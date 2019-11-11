import pandas as pd
import numpy as np

# name of the files we want to reformat
f1 = 'data/labels_BP.csv'
f2 = 'data/labels_CC.csv'
f3 = 'data/labels_MF.csv'
f4 = 'data/conditions_annotation.csv'


def file_formater(df):
    # reads the csv file into a dataframe
    df = pd.DataFrame(pd.read_csv(f4))
    print(df)
    # combine the rows of the localization of genes only for (BP, CC, MF)
    rsf1 = df.melt(id_vars=['gene', 'validation'], var_name='loc', value_name='localization')
    print(rsf1)
    # input into a dataframe
    rsf2 = pd.DataFrame(rsf1)
    print(rsf2)
    # drops the var name column called loc
    rsf3 = rsf2.drop('loc', axis=1)
    print(rsf3)
    # drop all duplicates
    rsf4 = rsf3.drop_duplicates()
    print(rsf4)
    # generate new csv file
    rsf5 = rsf4.fillna('null')
    print(rsf5)
    rsf5.to_csv('data/rf_labels_BP.csv')


def file_condit(df):
    # -----ONLY FOR CONDITIONS TABLE BLOCK START---------
    # reads the csv file into a dataframe
    df = pd.DataFrame(pd.read_csv(f4))
    print(df)
    rsf1 = df.fillna('null')
    print(rsf1)
    rsf2 = pd.DataFrame(rsf1)
    rsf3 = rsf2.drop_duplicates()
    print(rsf3)
    rsf3.to_csv('data/rf_conditions_annotations.csv')
    # -----ONLY FOR CONDITIONS TABLE BLOCK END---------
    file_formater(f1)
    file_formater(f2)
    file_formater(f3)
    file_condit(f4)
