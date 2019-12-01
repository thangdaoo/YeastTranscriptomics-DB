import pymysql as ps
import pandas as pd
import plotly.graph_objects as go


def make_connection():
    return ps.connect(host='yeast-transcriptomes.czfisxdhgfsf.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='qJ6D2qwzjhbdwic',
                      port=3306, autocommit=True)


cnx = make_connection()
cur = cnx.cursor()
# ----------BAR GRAPH FOR SC EXPRESSION--------------------------
cur.execute('USE yeast_transcriptomesDB');
cur.execute(
    "SELECT SC_ID, Gene_ID, Condit_ID, SC_Expression FROM ( select SC_ID, Gene_ID, Condit_ID, SC_Expression, DENSE_RANK() OVER (PARTITION BY Condit_ID ORDER BY SC_ID) as r FROM SC_Expression) AS t WHERE t.r <= 5 ORDER BY SC_ID")
ALL = cur.fetchall()
sc_id = []
gene_id = []
condit_id = []
sc_expression = []

for x in ALL:
    startinfo = str(x).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "")
    splitinfo = startinfo.split(',')
    # print(splitinfo)
    sc_id.append(splitinfo[0])
    gene_id.append(splitinfo[1])
    condit_id.append(splitinfo[2])
    sc_expression.append(splitinfo[3])
df = pd.DataFrame({
    'Condition ID': condit_id,
    'Gene Name': gene_id,
    'SC_Expression': sc_expression

})
cd = df['Condition ID'].to_numpy()
cd = list(cd)
gn = df['Gene Name'].to_numpy()
gn = list(gn)
sc = df['SC_Expression'].to_numpy(dtype=float)
sc = list(sc)
# print(cd)
# print(gn)
# print(sc)
total = 100
x = cd[0:total]
y = sc[0:total]
cur.execute("SELECT Condit_ID,PrimaryComponent FROM Conditions_Annotations")
hover = cur.fetchall()
i = 0
for x in hover:
    startinfo = str(x).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "")
    splitinfo = startinfo.split(',')
    condit = splitinfo[0]
    prim = splitinfo[1]
fig = go.Figure()
start = 0
end = 4
while (start != total):
    fig.add_trace(go.Bar(x=gn[start:end], y=sc[start:end], name=cd[start]))
    start += 5
    end += 5

fig.update_layout(barmode='stack', xaxis_title='Gene Name', xaxis={'categoryorder': 'category ascending'},
                  title={'text': 'Expression in Yeast Genes', 'y': 0.9, 'x': 0.5, 'xanchor': 'center',
                         'yanchor': 'top'},
                  yaxis=dict(title='TPM (transcripts per million)'))
fig.show()
# --------------END BAR GRAPH SC EXPRESSION
