import pymysql as ps
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from ipywidgets import widgets
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import container

import pandas as pd
import matplotlib.pyplot as plt
import pymysql as ps
from matplotlib.ticker import FormatStrFormatter
import numpy as np


# create a list of samples
# samples = []
# df = pd.read_csv('data/conditions_annotation.csv')
# for x in df['ID']:
#     print(x)
#     samples.append(x)
#     # print(df['ID'])
# print(samples)

# def make_connection():
#     return ps.connect(host='yeast-transcriptomes.czfisxdhgfsf.us-east-1.rds.amazonaws.com', user='admin',
#                       passwd='qJ6D2qwzjhbdwic',
#                       port=3306, autocommit=True)
#
# cnx = make_connection()
# cur = cnx.cursor()
# sql = "SELECT * FROM Conditions_Annotations"
# cur.execute(sql)
# result = cur.fetchall()
# for row in result:
#     record = {
#         'Condit_ID': row[0],
#         'PrimaryComponent': row[1],
#         'SecondaryComponent': row[2],
#         'Additional_Info': row[3]
#     }
#     print(row)
#
# cur.close()
# cnx.commit()
# cnx.close()

# d = pd.read_csv('data/rf_SC_expressions.csv')
# sc_expression = d['SC_Expression']
# condit_id = d['Condition_ID']
# plt.figure(figsize=(85,10))
# plt.scatter(condit_id,sc_expression)
# plt.xlabel('Condition ID')
# plt.ylabel('Expression Value')
# plt.show()


# def make_connection():
#     return ps.connect(host='yeast-transcriptomes.czfisxdhgfsf.us-east-1.rds.amazonaws.com', user='admin',
#                       passwd='qJ6D2qwzjhbdwic',
#                       port=3306, autocommit=True)
#
#
# cnx = make_connection()
# cur = cnx.cursor()
#
# # x-axis
# cur.execute('USE yeast_transcriptomesDB');
# cur.execute("SELECT DISTINCT(Condit_ID) FROM SC_Expression")
# Condit_ID = cur.fetchall()
# condit_list = []
# for condit in Condit_ID:
#     startinfo = str(condit).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "").replace(",", "")
#     condit_list.append(startinfo)
#
# # y-axis
# master_gene = []
# master_sc = []
# for condit in condit_list:
#     # print(condit)
#     cur.execute('USE yeast_transcriptomesDB');
#     cur.execute("SELECT Gene_ID FROM SC_Expression WHERE Condit_ID = '%s' " % condit)
#     Gene_ID = cur.fetchall()
#     gene_list = []
#     for gene in Gene_ID:
#         startinfo = str(gene).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "").replace(",", "")
#         gene_list.append(startinfo)
#     master_gene.append(gene_list)
#
#     cur.execute('USE yeast_transcriptomesDB');
#     cur.execute("SELECT SC_Expression FROM SC_Expression WHERE Condit_ID ='%s' " % condit)
#     SC_Expression = cur.fetchall()
#     sc_list = []
#     for SC in SC_Expression:
#         startinfo = str(SC).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "").replace(",", "")
#         sc_list.append(startinfo)
#     master_sc.append(sc_list)
# df = pd.DataFrame({'Condition_ID' : condit_list,
#                    'Gene_ID' : master_gene,
#                    'SC_Expression' : master_sc})


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

result = [nullCount,verifiedCount,dubiousCount,uncharCount,vsgCount]
x_axis = [1,2,3,4,5]

plt.bar(x_axis,result,align='center')
plt.xticks(x_axis,validationList,rotation=45)
fig, ax = plt.subplots()
plt.xlabel('Validation')
plt.ylabel('Count')
plt.show()
