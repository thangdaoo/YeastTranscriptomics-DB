import pandas as pd
#as needed depends on data
f1 = 'data/rf_labels_BP.csv'
f2 = 'data/rf_labels_CC.csv'
f3 = 'data/rf_labels_MF.csv'
df1 = pd.read_csv(f1)
df2 = pd.read_csv(f2)
df3 = pd.read_csv(f3)
rsf1 = pd.DataFrame(df1)
rsf2 = pd.DataFrame(df2)
rsf3 = pd.DataFrame(df3)
rsf1 = rsf1.drop('Unnamed: 0', axis=1)
rsf2 = rsf2.drop('Unnamed: 0', axis=1)
rsf3 = rsf3.drop('Unnamed: 0', axis=1)
# merge the first two files together by gene
first_merge = pd.merge(left=rsf1, right=rsf2, left_on='gene', right_on='gene')
# take the initial merge and merge it with the last file
second_merge = pd.merge(left=first_merge, right=rsf3, left_on='gene', right_on='gene')
# print(second_merge)
final = pd.DataFrame(second_merge)

final = final.drop(['validation_y', 'validation', ], axis=1)
final = final.rename(columns={'validation_x': 'validation', 'localization_x': 'Biological_process',
                              'localization_y': 'Cellular_component', 'localization': 'Molecular_function'})
final = final.drop_duplicates()
final = final.fillna('null')
print(final)
final.to_csv('data/combined_BP_CC_MF.csv')
# final = pd.DataFrame(final)
# final.to_csv('output.csv')
# combine the rows of the localization of genes only for (BP, CC, MF)
# rsf1 = df.melt(id_vars=['gene','validation'],var_name='loc',value_name='localization')
# print(rsf1)
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
# rsf5 = rsf4.fillna('null')
# print(rsf5)
