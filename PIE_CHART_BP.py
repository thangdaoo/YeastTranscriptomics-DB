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
for x in pt:
    while (bc):
        npt.append("")
        bc = False
    npt.append(x)
print(total)

labels = bp
values = total
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()
