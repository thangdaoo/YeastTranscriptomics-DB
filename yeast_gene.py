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
cur.execute('''CREATE TABLE Conditions_Annotations ( Condit_ID VARCHAR(30) NOT NULL PRIMARY KEY,PrimaryComponent VARCHAR(30),SecondaryComponent VARCHAR(30),Additonal_Information VARCHAR(30));''');
cur.execute('''CREATE TABLE Yeast_Gene (Gene_ID VARCHAR(30) NOT NULL PRIMARY KEY, Validation VARCHAR(30)    ,Molecular_Function VARCHAR(30),Biological_Process VARCHAR(30),Cellular_Component VARCHAR(30),SC_Expression VARCHAR(30));''')
cur.execute('''CREATE TABLE SC_Expression (SC_ID VARCHAR(30) NOT NULL PRIMARY KEY,Gene_ID VARCHAR(30),Condit_ID VARCHAR(30), FOREIGN KEY(Condit_ID) REFERENCES Conditions_Annotations(Condit_ID),FOREIGN KEY(Gene_ID) REFERENCES Yeast_Gene(Gene_ID));''')
cur.execute('''CREATE TABLE Localization (Localization_ID VARCHAR(30) NOT NULL PRIMARY  KEY,Biological_Process_Loc VARCHAR(100),Cellular_Component_Loc VARCHAR(100),Molecular_Function VARCHAR(100), Localization_Name VARCHAR(100));''')
cur.execute('''CREATE TABLE YeastGene_Localization(Process_ID VARCHAR(30) NOT NULL PRIMARY KEY,Gene_ID VARCHAR(30), Localization_ID VARCHAR(30),FOREIGN KEY(Gene_ID) REFERENCES Yeast_Gene(Gene_ID),FOREIGN KEY(Localization_ID) REFERENCES Localization(Localization_ID));''')