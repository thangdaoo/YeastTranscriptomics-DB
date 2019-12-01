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

fig = go.Figure(go.Funnel(
    y=val,
    x=total,
))

fig.show()
