import pandas as pd
import plotly.graph_objects as go
import pymysql as ps


def make_connection():
    return ps.connect(host='yeast-transcriptomes.czfisxdhgfsf.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='qJ6D2qwzjhbdwic',
                      port=3306, autocommit=True)


cnx = make_connection()
cur = cnx.cursor()
cur.execute('USE yeast_transcriptomesDB');
cur.execute(
    "SELECT COUNT(GENE_ID) as 'Total', Molecular_Function FROM Yeast_Gene yg GROUP BY yg.Molecular_Function ORDER BY Total DESC")
ALL = cur.fetchall()
mf = []
total = []
for x in ALL:
    startinfo = str(x).replace(')', '').replace('(', '').replace('u\'', '').replace('n\'', '').replace("\\", "").replace("'","")
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
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_layout(
    title_text="Molecular Functions found in Genes", )
fig.show()
