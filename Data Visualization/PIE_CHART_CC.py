import matplotlib.pyplot as plt
import pymysql as ps
import plotly.graph_objects as go
import pandas as pd

def make_connection():
    return ps.connect(host='yeast-transcriptomes.czfisxdhgfsf.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='qJ6D2qwzjhbdwic',
                      port=3306, autocommit=True)


cnx = make_connection()
cur = cnx.cursor()
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
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.update_layout(
    title_text="Gene Localizations",)
fig.show()
