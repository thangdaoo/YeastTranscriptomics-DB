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

# Drop Existing Tables
# cur.execute('DROP TABLE IF EXISTS Conditions_Annotations');
# cur.execute('DROP TABLE IF EXISTS Yeast_Gene');
# cur.execute('DROP TABLE IF EXISTS Localization');
# cur.execute('DROP TABLE IF EXISTS SC_Expression');
# cur.execute('DROP TABLE IF EXISTS YeastGene_Localization');
# Create Regular Table
cur.execute('''CREATE TABLE Conditions_Annotations (Condit_ID VARCHAR(30) NOT NULL PRIMARY KEY,PrimaryComponent VARCHAR(30),SecondaryComponent VARCHAR(30),Additional_Information VARCHAR(30));''')
cur.execute('''CREATE TABLE Yeast_Gene (Gene_ID VARCHAR(30) NOT NULL PRIMARY KEY,Validation VARCHAR(30),Molecular_Function VARCHAR(30),Biological_Process VARCHAR(30),Cellular_Component VARCHAR(30), SC_Expression VARCHAR(30));''')
cur.execute('''CREATE TABLE Localization (Localization_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,Biological_Process_Loc VARCHAR(30),Cellular_Component_Loc VARCHAR(30),Molecular_Function VARCHAR(30));''')
# Create Join Tables
# cur.execute('''CREATE TABLE SC_Expression (SC_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,Gene_ID VARCHAR(30),Condit_ID VARCHAR(30), FOREIGN KEY(Gene_ID) REFERENCES Yeast_Gene(Gene_ID),FOREIGN KEY(Condit_ID) REFERENCES Conditions_Annotations(Condit_ID));''')
# cur.execute('''CREATE TABLE YeastGene_Localization (YeastGeneLoc_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Gene_ID VARCHAR(30), Localization_ID VARCHAR(30), FOREIGN KEY(Gene_ID) REFERENCES Yeast_Gene(Gene_ID),FOREIGN KEY(Localization_ID) REFERENCES Localization(Localization_ID));''')

# Data Parser
with open("data/conditions_annotation.csv", 'r') as r1:
    for line in r1:
        line = line.split(',')
        if(len(line) == 3):
            ID = line.__getitem__(0)
            primary = line.__getitem__(1)
            secondary = line.__getitem__(2)
            addition_info = 'null'
            cur.execute('INSERT IGNORE INTO Conditions_Annotations(Condit_ID,PrimaryComponent,SecondaryComponent,Additional_Information) VALUES (%s,%s,%s,%s)',(ID, primary, secondary, addition_info))
        if(len(line) == 4):
            ID = line.__getitem__(0)
            primary = line.__getitem__(1)
            secondary = line.__getitem__(2)
            addition_info = line.__getitem__(3)
            cur.execute('INSERT IGNORE INTO Conditions_Annotations(Condit_ID,PrimaryComponent,SecondaryComponent,Additional_Information) VALUES (%s,%s,%s,%s)',(ID, primary, secondary, addition_info))
        # print(ID, primary, secondary, addition_info)

with open("data/labels_BP.csv", 'r') as r2:
    for line in r2:
        line = line.split(',')
        if len(line) == 2:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            loc1 = 'null'
            cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (gene_name, validation))
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc1)
            # print(ID, validation, loc1)
        if len(line) == 3:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            loc1 = line.__getitem__(2)
            cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (gene_name, validation))
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc1)
            # print(ID, validation, loc1)
        if len(line) == 4:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            loc1 = line.__getitem__(2)
            loc2 = line.__getitem__(3)
            # cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (gene_name, validation))
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc1)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc2)
            # print(ID, validation, loc1, loc2)
        if len(line) == 5:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            loc1 = line.__getitem__(2)
            loc2 = line.__getitem__(3)
            loc3 = line.__getitem__(4)
            # cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (gene_name, validation))
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc1)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc2)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc3)
            # print(ID, validation, loc1, loc2, loc3)
        if len(line) == 6:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            loc1 = line.__getitem__(2)
            loc2 = line.__getitem__(3)
            loc3 = line.__getitem__(4)
            loc4 = line.__getitem__(5)
            # cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (gene_name, validation))
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc1)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc2)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc3)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc4)
            # print(ID, validation, loc1, loc2, loc3, loc4)
        if len(line) == 7:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            loc1 = line.__getitem__(2)
            loc2 = line.__getitem__(3)
            loc3 = line.__getitem__(4)
            loc4 = line.__getitem__(5)
            loc5 = line.__getitem__(6)
            # cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (gene_name, validation))
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc1)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc2)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc3)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc4)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc5)
            # print(ID, validation, loc1, loc2, loc3, loc4, loc5)
        if len(line) == 8:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            loc1 = line.__getitem__(2)
            loc2 = line.__getitem__(3)
            loc3 = line.__getitem__(4)
            loc4 = line.__getitem__(5)
            loc5 = line.__getitem__(6)
            loc6 = line.__getitem__(7)
            # cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (gene_name, validation))
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc1)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc2)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc3)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc4)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc5)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc6)
            # print(ID, validation, loc1, loc2, loc3, loc4, loc5, loc6)
        if len(line) == 9:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            loc1 = line.__getitem__(2)
            loc2 = line.__getitem__(3)
            loc3 = line.__getitem__(4)
            loc4 = line.__getitem__(5)
            loc5 = line.__getitem__(6)
            loc6 = line.__getitem__(7)
            loc7 = line.__getitem__(8)
            # cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (gene_name, validation))
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc1)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc2)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc3)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc4)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc5)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc6)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc7)
            # print(ID, validation, loc1, loc2, loc3, loc4, loc5, loc6, loc7)
        if len(line) == 10:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            loc1 = line.__getitem__(2)
            loc2 = line.__getitem__(3)
            loc3 = line.__getitem__(4)
            loc4 = line.__getitem__(5)
            loc5 = line.__getitem__(6)
            loc6 = line.__getitem__(7)
            loc7 = line.__getitem__(8)
            loc8 = line.__getitem__(9)
            # cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (gene_name, validation))
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc1)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc2)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc3)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc4)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc5)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc6)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc7)
            cur.execute('INSERT IGNORE INTO Localization(Biological_Process_Loc) VALUES (%s)', loc8)
            # print(ID, validation, loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8)

with open("data/labels_MF.csv",'r') as r3:
    for line in r3:
        line = line.split(',')
        if len(line) == 2:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            molecularFunction1 = 'null'
            cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (ID, validation))
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction1)
            # print(ID, validation, molecularFunction1)
        if len(line) == 3:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            molecularFunction1 = line.__getitem__(2)
            cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (ID, validation))
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction1)
            # print(ID, validation, molecularFunction1)
        if len(line) == 4:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            molecularFunction1 = line.__getitem__(2)
            molecularFunction2 = line.__getitem__(3)
            cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (ID, validation))
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction1)
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction2)
            # print(ID, validation, molecularFunction1, molecularFunction2)
        if len(line) == 5:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            molecularFunction1 = line.__getitem__(2)
            molecularFunction2 = line.__getitem__(3)
            molecularFunction3 = line.__getitem__(4)
            cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (ID, validation))
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction1)
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction2)
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction3)
            # print(ID, validation, molecularFunction1, molecularFunction2, molecularFunction3)
        if len(line) == 6:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            molecularFunction1 = line.__getitem__(2)
            molecularFunction2 = line.__getitem__(3)
            molecularFunction3 = line.__getitem__(4)
            molecularFunction4 = line.__getitem__(5)
            cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (ID, validation))
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction1)
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction2)
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction3)
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction4)
            # print(ID, validation, molecularFunction1, molecularFunction2, molecularFunction3, molecularFunction4)
        if len(line) == 7:
            ID = line.__getitem__(0)
            validation = line.__getitem__(1)
            molecularFunction1 = line.__getitem__(2)
            molecularFunction2 = line.__getitem__(3)
            molecularFunction3 = line.__getitem__(4)
            molecularFunction4 = line.__getitem__(5)
            molecularFunction5 = line.__getitem__(6)
            cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation) VALUES (%s,%s)', (ID, validation))
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction1)
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction2)
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction3)
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction4)
            cur.execute('INSERT IGNORE INTO Localization(Molecular_Function) VALUES (%s)', molecularFunction5)
            # print(ID, validation, molecularFunction1, molecularFunction2, molecularFunction3, molecularFunction4, molecularFunction5)

# with open("data/labels_CC.csv","r") as r4:
#     for line in r3:
#         line = line.split(',')
#         # print(line,len(line))
#         if (len(line) == 2):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = 'null'
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)', (gene_name,loc1))
#             print(gene_name, validation, loc1)
#         if (len(line) == 3):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)', (gene_name,loc1))
#             print(gene_name, validation, loc1)
#         if (len(line) == 4):
#             gene_name = line.__getitem__(0)
#             validation = line.__getitem__(1)
#             loc1 = line.__getitem__(2)
#             loc2 = line.__getitem__(3)
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)', (gene_name,loc1))
#             cur.execute('INSERT IGNORE INTO Cellular_Component(Gene_name,Cellular_Component_Loc) VALUES (%s,%s)',
#                 (gene_name, loc2))
#             print(gene_name, validation, loc1, loc2)
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
#             print(gene_name, validation, loc1, loc2, loc3)
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
#             print(gene_name, validation, loc1, loc2, loc3, loc4)
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
#             print(gene_name, validation, loc1, loc2, loc3, loc4, loc5)
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
#             print(gene_name,validation,loc1,loc2,loc3,loc4,loc5,loc6)
#


cur.close()
cnx.commit()
cnx.close()
