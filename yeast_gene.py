import pymysql as ps
#name db = yeast-transcriptomes
#user_name = admin
# password: qJ6D2qwzjhbdwic

def make_connection():
    return ps.connect(host='yeast-transcriptomes.czfisxdhgfsf.us-east-1.rds.amazonaws.com', user='admin', passwd='qJ6D2qwzjhbdwic',
       port=3306, autocommit=True)

cnx = make_connection()
cur = cnx.cursor()

#Setting up tables
cur.execute('DROP DATABASE IF EXISTS yeast_transcriptomesDB');
cur.execute('CREATE DATABASE yeast_transcriptomesDB');
cur.execute('USE yeast_transcriptomesDB');

#create tables
#cur.execute("DROP TABLE IF EXISTS Conditions_Annotations");
#cur.execute('DROP TABLE IF EXISTS Yeast_gene');
#cur.execute('DROP TABLE IF EXISTS SC_Expression');
#cur.execute('DROP TABLE IF EXISTS YeastGene-Localization');
#cur.execute("DROP TABLE IF EXISTS Localization");
cur.execute('''CREATE TABLE Conditions_Annotations (Condit_ID VARCHAR(30) NOT NULL PRIMARY KEY,PrimaryComponent VARCHAR(30),SecondaryComponent VARCHAR(30),Additional_Information VARCHAR(30));''')
cur.execute('''CREATE TABLE Yeast_Gene (Gene_name VARCHAR(30) NOT NULL PRIMARY KEY,Validation VARCHAR(30));''')
cur.execute('''CREATE TABLE Condition_Gene (Expression DOUBLE,Gene_name VARCHAR(30) NOT NULL ,Condit_ID VARCHAR(30) NOT NULL,FOREIGN KEY(Condit_ID) REFERENCES Conditions_Annotations(Condit_ID),FOREIGN KEY(Gene_name) REFERENCES Yeast_Gene(Gene_name), PRIMARY KEY (Gene_name,Condit_ID));''')
# cur.execute('''CREATE TABLE Localization (Localization_ID VARCHAR(30) NOT NULL PRIMARY  KEY,Biological_Process_Loc VARCHAR(100),Cellular_Component_Loc VARCHAR(100),Molecular_Function VARCHAR(100), Localization_Name VARCHAR(100));''')
cur.execute('''CREATE TABLE Biology_Process (ID INT NOT NULL AUTO_INCREMENT,PRIMARY KEY (ID),Gene_name VARCHAR(30) NOT NULL,Biological_Process_Loc VARCHAR(100));''')
cur.execute('''CREATE TABLE Molecular_Function (Gene_name VARCHAR(30) NOT NULL,Molecular_Function_Loc VARCHAR(100));''')
cur.execute('''CREATE TABLE Cellular_Component (Gene_name VARCHAR(30) NOT NULL,Cellular_Component_Loc VARCHAR(100));''')
#cur.execute('''CREATE TABLE Yeast_Gene_Biology_Process (Gene_ID INT NOT NULL, FOREIGN KEY(Gene_ID) REFERENCES Yeast_Gene(ID),Gene_name VARCHAR(30) NOT NULL, FOREIGN KEY(Gene_name) REFERENCES Biology_Process(Gene_name));''')
#cur.execute('''CREATE TABLE Yeast_Gene_Molecular_Function (Gene_name VARCHAR(30) NOT NULL, FOREIGN KEY(Gene_name) REFERENCES Yeast_Gene(Gene_name),MF_ID INT NOT NULL, FOREIGN KEY(MF_ID) REFERENCES Molecular_Function(ID));''')
#cur.execute('''CREATE TABLE Yeast_Gene_Cellular_Component (Gene_name VARCHAR(30) NOT NULL, FOREIGN KEY(Gene_name) REFERENCES Yeast_Gene(Gene_name),CC_ID INT NOT NULL, FOREIGN KEY(CC_ID) REFERENCES Cellular_Component(ID));''')
#cur.execute('''CREATE TABLE YeastGene_Localization(Process_ID VARCHAR(30) NOT NULL PRIMARY KEY,Gene_ID VARCHAR(30), Localization_ID VARCHAR(30),FOREIGN KEY(Gene_ID) REFERENCES Yeast_Gene(Gene_ID),FOREIGN KEY(Localization_ID) REFERENCES Localization(Localization_ID));''')



#data parser
# with open("Yeast Transcriptomics Data/conditions_annotation.csv",'r') as r1:
#     for line in r1:
#         line = line.split(',')
#         print(line,len(line))
#         if(len(line) == 3):
#             ID = line.__getitem__(0)
#             primary = line.__getitem__(1)
#             secondary = line.__getitem__(2)
#             addition_info = 'null'
#             cur.execute('INSERT IGNORE INTO Conditions_Annotations(Condit_ID,PrimaryComponent,SecondaryComponent,Additional_Information) VALUES (%s,%s,%s,%s)',(ID, primary, secondary, addition_info))
#         if(len(line) == 4):
#             ID = line.__getitem__(0)
#             primary = line.__getitem__(1)
#             secondary = line.__getitem__(2)
#             addition_info = line.__getitem__(3)
#             cur.execute('INSERT IGNORE INTO Conditions_Annotations(Condit_ID,PrimaryComponent,SecondaryComponent,Additional_Information) VALUES (%s,%s,%s,%s)',(ID, primary, secondary, addition_info))
#         print(ID,primary,secondary,addition_info)
#
# with open("Yeast Transcriptomics Data/labels_BP.csv", 'r') as r2:
#     for line in r2:
#         line = line.split(',')
#         if (len(line) == 2):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = 'null'
#             cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_name,Validation) VALUES (%s,%s)', (gene_name, validation))
#             # cur.execute('INSERT IGNORE INTO Yeast_Gene_Biology_Process(Gene_ID,Gene_name) VALUES (%s,%s)', (gene_name))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc1))
#         if(len(line)==3):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_name,Validation) VALUES (%s,%s)',(gene_name,validation))
#             #cur.execute('INSERT IGNORE INTO Yeast_Gene_Biology_Process(Gene_ID,Gene_name) VALUES (%s,%s)', (gene_name))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)', (gene_name,loc1))
#         if (len(line) == 4):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_name,Validation) VALUES (%s,%s)', (gene_name, validation))
#             # cur.execute('INSERT IGNORE INTO Yeast_Gene_Biology_Process(Gene_ID,Gene_name) VALUES (%s,%s)', (gene_name))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',(gene_name, loc1))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',(gene_name, loc2))
#         if (len(line) == 5):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             loc3 = line.__getitem__(4)
#             cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_name,Validation) VALUES (%s,%s)',
#                         (gene_name, validation))
#             # cur.execute('INSERT IGNORE INTO Yeast_Gene_Biology_Process(Gene_ID,Gene_name) VALUES (%s,%s)', (gene_name))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc1))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc2))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc3))
#         if (len(line) == 6):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             loc3 = line.__getitem__(4)
#             loc4 = line.__getitem__(5)
#             cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_name,Validation) VALUES (%s,%s)',
#                         (gene_name, validation))
#             # cur.execute('INSERT IGNORE INTO Yeast_Gene_Biology_Process(Gene_ID,Gene_name) VALUES (%s,%s)', (gene_name))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc1))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc2))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc3))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc4))
#         if (len(line) == 7):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             loc3 = line.__getitem__(4)
#             loc4 = line.__getitem__(5)
#             loc5 = line.__getitem__(6)
#             cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_name,Validation) VALUES (%s,%s)',
#                         (gene_name, validation))
#             # cur.execute('INSERT IGNORE INTO Yeast_Gene_Biology_Process(Gene_ID,Gene_name) VALUES (%s,%s)', (gene_name))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc1))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc2))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc3))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc4))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc5))
#         if (len(line) == 8):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             loc3 = line.__getitem__(4)
#             loc4 = line.__getitem__(5)
#             loc5 = line.__getitem__(6)
#             loc6 = line.__getitem__(7)
#             cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_name,Validation) VALUES (%s,%s)',
#                         (gene_name, validation))
#             # cur.execute('INSERT IGNORE INTO Yeast_Gene_Biology_Process(Gene_ID,Gene_name) VALUES (%s,%s)', (gene_name))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc1))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc2))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc3))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc4))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc5))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc6))
#         if (len(line) == 9):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             loc3 = line.__getitem__(4)
#             loc4 = line.__getitem__(5)
#             loc5 = line.__getitem__(6)
#             loc6 = line.__getitem__(7)
#             loc7 = line.__getitem__(8)
#             cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_name,Validation) VALUES (%s,%s)',
#                         (gene_name, validation))
#             # cur.execute('INSERT IGNORE INTO Yeast_Gene_Biology_Process(Gene_ID,Gene_name) VALUES (%s,%s)', (gene_name))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc1))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc2))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc3))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc4))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc5))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc6))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc7))
#         if (len(line) == 10):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             loc3 = line.__getitem__(4)
#             loc4 = line.__getitem__(5)
#             loc5 = line.__getitem__(6)
#             loc6 = line.__getitem__(7)
#             loc7 = line.__getitem__(8)
#             loc8 = line.__getitem__(9)
#             cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_name,Validation) VALUES (%s,%s)',
#                         (gene_name, validation))
#             # cur.execute('INSERT IGNORE INTO Yeast_Gene_Biology_Process(Gene_ID,Gene_name) VALUES (%s,%s)', (gene_name))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc1))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc2))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc3))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc4))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc5))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc6))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc7))
#             cur.execute('INSERT IGNORE INTO Biology_Process(Gene_name,Biological_Process_Loc) VALUES (%s,%s)',
#                         (gene_name, loc8))
#         #print(line,len(line))
#         # gene = line.__getitem__(0)
#         # validation = line.__getitem__(1)
#         # localization = line.__getitem__(2)
#         # print(gene,validation,localization)
# with open("Yeast Transcriptomics Data/labels_CC.csv","r") as r3:
#     for line in r3:
#         line = line.split(',')
#         print(line,len(line))
#         if (len(line) == 2):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = 'null'
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)', (gene_name,loc1))
#         if (len(line) == 3):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)', (gene_name,loc1))
#         if (len(line) == 4):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)', (gene_name,loc1))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                 (gene_name, loc2))
#         if (len(line) == 5):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             loc3 = line.__getitem__(4)
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)', (gene_name,loc1))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                 (gene_name, loc2))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                 (gene_name, loc3))
#         if (len(line) == 6):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             loc3 = line.__getitem__(4)
#             loc4 = line.__getitem__(5)
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)', (gene_name,loc1))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                 (gene_name, loc2))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                 (gene_name, loc3))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                 (gene_name, loc4))
#         if (len(line) == 7):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             loc3 = line.__getitem__(4)
#             loc4 = line.__getitem__(5)
#             loc5 = line.__getitem__(6)
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                         (gene_name, loc1))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                         (gene_name, loc2))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                         (gene_name, loc3))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                         (gene_name, loc4))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                         (gene_name, loc5))
#         if (len(line) == 8):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             loc3 = line.__getitem__(4)
#             loc4 = line.__getitem__(5)
#             loc5 = line.__getitem__(6)
#             loc6 = line.__getitem__(7)
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',(gene_name, loc1))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',(gene_name, loc2))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',(gene_name, loc3))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                         (gene_name, loc4))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                         (gene_name, loc5))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                         (gene_name, loc6))
cur.close()
cnx.commit()
cnx.close()