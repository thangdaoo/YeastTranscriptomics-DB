import pymysql as ps
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from ipywidgets import widgets
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import container


def make_connection():
    return ps.connect(host='yeast-transcriptomes.czfisxdhgfsf.us-east-1.rds.amazonaws.com', user='admin',
                      passwd='qJ6D2qwzjhbdwic',
                      port=3306, autocommit=True)


cnx = make_connection()
cur = cnx.cursor()

# x-axis
cur.execute('USE yeast_transcriptomesDB');
cur.execute("SELECT DISTINCT(Condit_ID) FROM SC_Expression")
Condit_ID = cur.fetchall()
condit_list = []
for condit in Condit_ID:
    startinfo = str(condit).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "").replace(",", "")
    condit_list.append(startinfo)

# y-axis
master_gene = []
master_sc = []
for condit in condit_list:
    # print(condit)
    cur.execute('USE yeast_transcriptomesDB');
    cur.execute("SELECT Gene_ID FROM SC_Expression WHERE Condit_ID = '%s' " % condit)
    Gene_ID = cur.fetchall()
    gene_list = []
    for gene in Gene_ID:
        startinfo = str(gene).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "").replace(",", "")
        gene_list.append(startinfo)
    master_gene.append(gene_list)

    cur.execute('USE yeast_transcriptomesDB');
    cur.execute("SELECT SC_Expression FROM SC_Expression WHERE Condit_ID ='%s' " % condit)
    SC_Expression = cur.fetchall()
    sc_list = []
    for SC in SC_Expression:
        startinfo = str(SC).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "").replace(",", "")
        sc_list.append(startinfo)
    master_sc.append(sc_list)
df = pd.DataFrame({'Condition_ID' : condit_list,
                   'Gene_ID' : master_gene,
                   'SC_Expression' : master_sc})







# cur.execute('USE yeast_transcriptomesDB');
# cur.execute("SELECT * FROM SC_Expression")
# ALL = cur.fetchall()
# table = []
# for x in ALL:
#     startinfo = str(x).replace(')', '').replace('(', '').replace('u\'', '').replace("'", "")
#     splitinfo = startinfo.split(',')
#     tableappend = splitinfo[0]+','+splitinfo[1]+','+ splitinfo[2]+','+ splitinfo[3]
#     table.append(tableappend)