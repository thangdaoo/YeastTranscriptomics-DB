import pandas as pd
import numpy as np
#name of the files we want to reformat
f1 = 'data/SC_expression.csv'
#reads the csv file into a dataframe
df = pd.DataFrame(pd.read_csv(f1))
print(df)
#combine the rows of the localization of genes
rsf1 = df.stack()
print(rsf1)
# #input into a dataframe
# rsf2 = pd.DataFrame(rsf1)
# print(rsf2)
# #drops the var name column called loc
# rsf3 = rsf2.drop('loc',axis=1)
# print(rsf3)
# #drop all duplicates
# rsf4 = rsf3.drop_duplicates()
# print(rsf4)
# #generate new csv file
# rsf4.to_csv('data/rf_labels_MF.csv')