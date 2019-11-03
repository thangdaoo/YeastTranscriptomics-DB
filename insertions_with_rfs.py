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
cur.execute('''CREATE TABLE Yeast_Gene (Gene_ID VARCHAR(30) NOT NULL PRIMARY KEY,Validation VARCHAR(30),Biological_Process VARCHAR(30),Cellular_Component VARCHAR(30),Molecular_Function VARCHAR(30), SC_Expression VARCHAR(30));''')
cur.execute('''CREATE TABLE Localization (Localization_ID INT NOT NULL PRIMARY KEY,Biological_Process_Loc VARCHAR(30),Cellular_Component_Loc VARCHAR(30),Molecular_Function VARCHAR(30));''')
# Create Join Tables
#cur.execute('''CREATE TABLE SC_Expression (SC_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,Gene_ID VARCHAR(30),Condit_ID VARCHAR(30), FOREIGN KEY(Gene_ID) REFERENCES Yeast_Gene(Gene_ID),FOREIGN KEY(Condit_ID) REFERENCES Conditions_Annotations(Condit_ID));''')
cur.execute('''CREATE TABLE YeastGene_Localization (Gene_local_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Gene_ID VARCHAR(30) NOT NULL, Localization_ID INT NOT NULL , FOREIGN KEY(Gene_ID) REFERENCES Yeast_Gene(Gene_ID),FOREIGN KEY(Localization_ID) REFERENCES Localization(Localization_ID));''')

#Data Parser
with open("data/rf_conditions_annotations.csv", 'r') as r1:
    next(r1)
    for line in r1:
        line = line.split(',')
        ID_num = line.__getitem__(0)
        sample_ID = line.__getitem__(1)
        primary = line.__getitem__(2)
        secondary = line.__getitem__(3)
        additional_info = line.__getitem__(4)
        #print(ID_num,sample_ID,primary,secondary,additional_info)
        cur.execute('INSERT IGNORE INTO Conditions_Annotations(Condit_ID,PrimaryComponent,SecondaryComponent,Additional_Information) VALUES (%s,%s,%s,%s)',(sample_ID, primary, secondary, additional_info))
with open("data/combined_BP_CC_MF.csv", 'r') as r1:
    #,gene,validation,Biological_process,Cellular_component,Molecular_function
    next(r1)
    for line in r1:
        line = line.split(',')
        ID_num = int(line.__getitem__(0))+1
        ID_num = str(ID_num)
        gene = line.__getitem__(1)
        valid = line.__getitem__(2)
        bp = line.__getitem__(3)
        cc = line.__getitem__(4)
        mf = line.__getitem__(5)
        cur.execute('INSERT IGNORE INTO Yeast_Gene(Gene_ID,Validation, Biological_Process,Cellular_Component,Molecular_Function) VALUES (%s,%s,%s,%s,%s)',(gene, valid,bp,cc,mf))
        cur.execute('INSERT IGNORE INTO Localization(Localization_ID,Biological_Process_Loc,Cellular_Component_Loc,Molecular_Function) VALUES (%s,%s,%s,%s)',(ID_num, bp, cc, mf))
        cur.execute('INSERT IGNORE INTO YeastGene_Localization(Gene_ID,Localization_ID) VALUES (%s,%s)',(gene,ID_num))

cur.close()
cnx.commit()
cnx.close()
