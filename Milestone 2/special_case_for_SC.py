import pandas as pd
import numpy as np

# name of the files we want to reformat
f1 = 'data/SC_expression.csv'
# reads the csv file into a dataframe
df = pd.DataFrame(pd.read_csv(f1))
print(df)
# drops duplicates within the dataframe
rsf1 = df.drop_duplicates()
# print(rsf1.melt(id_vars='gene'))
# reformat csv file
rsf2 = rsf1.melt(id_vars='gene')
rsf3 = pd.DataFrame(rsf2)
rsf3 = rsf3.rename(columns={'gene': 'Gene_ID', 'variable': 'Condition_ID', 'value': 'SC_Expression'})
print(rsf3)
rsf4 = rsf3.drop_duplicates()
# csv out to a new csv file
rsf4.to_csv('data/rf_SC_expressions.csv')
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
