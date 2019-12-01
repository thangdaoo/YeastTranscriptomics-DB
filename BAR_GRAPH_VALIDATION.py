import matplotlib.pyplot as plt
import pymysql as ps


def make_connection():
    return ps.connect(host='yeast-transcriptomes.czfisxdhgfsf.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='qJ6D2qwzjhbdwic',
                      port=3306, autocommit=True)


cnx = make_connection()
cur = cnx.cursor()

cur.execute('USE yeast_transcriptomesDB');
cur.execute("SELECT Gene_ID FROM Yeast_Gene WHERE Validation = 'null'")
null = cur.fetchall()
nullList = [list(i) for i in null]
nullCount = 0
for x in null:
    nullCount += 1

cur.execute("SELECT Gene_ID FROM Yeast_Gene WHERE Validation = 'Verified'")
verified = cur.fetchall()
verifiedList = [list(i) for i in verified]
verifiedCount = 0
for x in verified:
    verifiedCount += 1

cur.execute("SELECT Gene_ID FROM Yeast_Gene WHERE Validation = 'Dubious'")
dubious = cur.fetchall()
dubiousList = [list(i) for i in dubious]
dubiousCount = 0
for x in dubious:
    dubiousCount += 1

cur.execute("SELECT Gene_ID FROM Yeast_Gene WHERE Validation = 'Uncharacterized'")
unchar = cur.fetchall()
uncharList = [list(i) for i in unchar]
uncharCount = 0
for x in unchar:
    uncharCount += 1

cur.execute("SELECT Gene_ID FROM Yeast_Gene WHERE Validation = 'Verified|silenced_gene'")
vsg = cur.fetchall()
vsgList = [list(i) for i in vsg]
vsgCount = 0
for x in vsg:
    vsgCount += 1

cur.execute("SELECT DISTINCT Validation FROM Yeast_Gene")
validation = cur.fetchall()
validationList = [list(i) for i in validation]
validationCount = 0
for x in validationList:
    validationCount += 1

result = [nullCount, verifiedCount, dubiousCount, uncharCount, vsgCount]
x_axis = [1, 2, 3, 4, 5]

plt.bar(x_axis, result, align='center')
plt.xticks(x_axis, validationList, rotation=45)
fig, ax = plt.subplots()
plt.xlabel('Validation')
plt.ylabel('Count')
plt.show()
