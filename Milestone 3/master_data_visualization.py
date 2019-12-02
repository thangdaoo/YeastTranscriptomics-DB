from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pymysql as ps
import pandas as pd


def make_connection():
    return ps.connect(host='yeast-transcriptomes.czfisxdhgfsf.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='qJ6D2qwzjhbdwic',
                      port=3306, autocommit=True)


cnx = make_connection()
cur = cnx.cursor()

fig = make_subplots(
    rows=2, cols=3,
    subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4", "Plot 5", "Plot 6")
)
# ------------------SC EXPRESSION GRAPH START ---------------
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
start = 0
end = 4
while (start != total):
    fig.add_trace(go.Bar(x=gn[start:end], y=sc[start:end], name=cd[start]), row=1, col=1)
    start += 5
    end += 5

fig.update_layout(barmode='stack', xaxis_title='Gene Name', xaxis={'categoryorder': 'category ascending'},
                  title={'text': 'Expression in Genes', 'y': 0.9, 'x': 0.5, 'xanchor': 'center',
                         'yanchor': 'top'},
                  yaxis=dict(title='TPM (transcripts per million)'))

# ---------END SC EXPRESSION ------------------

# ----------START VALIDATION ----------------

cur.execute('USE yeast_transcriptomesDB');
cur.execute(
    "SELECT COUNT(GENE_ID) as 'Total', yg.Validation FROM Yeast_Gene yg GROUP BY yg.Validation ORDER BY Total DESC")
ALL = cur.fetchall()
val = []
total = []
for x in ALL:
    print(x)
    startinfo = str(x).replace(')', '').replace('(', '').replace('u\'', '').replace('n\'', '').replace("\\",
                                                                                                       "").replace("'",
                                                                                                                   "")
    splitinfo = startinfo.split(',')
    valtotal = splitinfo[0]
    mfn = splitinfo[1]
    total.append(valtotal)
    val.append(mfn)
    print(startinfo)
df = pd.DataFrame({
    'Total': total,
    'Validation': val

})

fig.add_trace(go.Bar(
    y=val,
    x=total,
    orientation='h',
), 1, 3)

# -----------END VALIDATION ------------------


# ------------START PIE BP-------------
cur.execute('USE yeast_transcriptomesDB');
cur.execute(
    "SELECT COUNT(Gene_ID) AS 'Total', Biological_Process FROM Yeast_Gene Group by Biological_Process ORDER BY Total DESC")

ALL = cur.fetchall()
bp = []
total = []
for x in ALL:
    startinfo = str(x).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "")
    splitinfo = startinfo.split(',')
    tbp = splitinfo[0]
    bpn = splitinfo[1]
    # print(splitinfo)
    total.append(tbp)
    bp.append(bpn)
df = pd.DataFrame({
    'Total': total,
    'Biological Process': bp

})
# print(df)
bp = df['Biological Process'].to_numpy()
total = df['Total'].to_numpy(dtype=int)
total = list(total)
pt = list(bp)
npt = list()
bc = True
bpn = list()

labels = bp
values = total

fig.add_trace(go.Pie(labels=labels, values=values, domain=dict(x=[0, .30], y=[0, .4])))
# ------------END PIE BP-------------
# -----------start cc---------------
cur.execute('USE yeast_transcriptomesDB');
cur.execute(
    "SELECT COUNT(*) as 'Total', Cellular_Component FROM Yeast_Gene GROUP BY Cellular_Component ORDER BY Total DESC")
ALL = cur.fetchall()
cc = []
total = []
for x in ALL:
    startinfo = str(x).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "")
    splitinfo = startinfo.split(',')
    tcc = splitinfo[0]
    ccn = splitinfo[1]
    # print(splitinfo)
    total.append(tcc)
    cc.append(ccn)
df = pd.DataFrame({
    'Total': total,
    'Cellular Component': cc

})
# print(df)
cc = df['Cellular Component'].to_numpy()
total = df['Total'].to_numpy(dtype=int)
total = list(total)
pt = list(cc)
npt = list()
bc = True
ccn = list()
for x in pt:
    while (bc):
        npt.append("")
        bc = False
    npt.append(x)
print(total)
labels = cc
values = total
fig.add_trace(go.Pie(labels=labels, values=values, domain=dict(x=[.35, 0.65], y=[0, .4])))
# e------------end cc-------------------
# e------------start mf-------------------
cur.execute('USE yeast_transcriptomesDB');
cur.execute(
    "SELECT COUNT(GENE_ID) as 'Total', Molecular_Function FROM Yeast_Gene yg GROUP BY yg.Molecular_Function ORDER BY Total DESC")
ALL = cur.fetchall()
mf = []
total = []
for x in ALL:
    startinfo = str(x).replace(')', '').replace('(', '').replace('u\'', '').replace('n\'', '').replace("\\",
                                                                                                       "").replace("'",
                                                                                                                   "")
    splitinfo = startinfo.split(',')
    tmf = splitinfo[0]
    mfn = splitinfo[1]
    total.append(tmf)
    mf.append(mfn)
df = pd.DataFrame({
    'Total': total,
    'Molecular Function': mf

})

mf = df['Molecular Function'].to_numpy()
total = df['Total'].to_numpy(dtype=int)
total = list(total)
pt = list(mf)
npt = list()
bc = True
mfn = list()
for x in pt:
    while (bc):
        npt.append("")
        bc = False
    npt.append(x)
# print(total)

labels = mf
values = total
fig.add_trace(go.Pie(labels=labels, values=values, domain=dict(x=[.70, 1], y=[0, .4])))
# e------------end mf-------------------
# fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
#               row=1, col=2)

# fig.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]),
#               row=2, col=1)

# fig.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]),
#               row=2, col=2)

fig.update_layout(height=1000, width=1400,
                  title_text="Multiple Subplots with Titles")
fig.update(layout_showlegend=False)
fig.show()
