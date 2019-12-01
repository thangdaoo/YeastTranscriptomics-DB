import matplotlib.pyplot as plt
import pymysql as ps
import plotly.graph_objects as go
import pandas as pd
import re

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
    print(x)
    startinfo = str(x).replace(')', '').replace('(', '').replace('n\', '').replace("\","")
    splitinfo = startinfo.split(',')
    tmf = splitinfo[0]
    mfn = re.sub("\n", "", splitinfo[1])
    # print(splitinfo)
    total.append(tmf)
    mf.append(mfn)
    print(startinfo)
df = pd.DataFrame({
    'Total': total,
    'Molecular Function': mf

})
# print(df)
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
print(total)

labels = mf
values = total
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_layout(
    title_text="Molecular Functions found in Genes",)
fig.show()
