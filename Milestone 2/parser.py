import pandas as pd

# name of the files we want to reformat
f1 = 'Yeast Data/labels_BP.csv'
f2 = 'Yeast Data/labels_CC.csv'
f3 = 'Yeast Data/labels_MF.csv'
f4 = 'Yeast Data/conditions_annotation.csv'
wf1 = 'Milestone 2/rf_labels_BP.csv'
wf2 = 'Milestone 2/rf_labels_CC.csv'
wf3 = 'Milestone 2/rf_labels_MF.csv'
wf4 = 'Milestone 2/rf_conditions_annotations.csv'


def file_formatter(df, writefile):
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
    rsf5.to_csv(writefile)


def file_condit(df, writefile):
    # -----ONLY FOR CONDITIONS TABLE BLOCK START---------
    # reads the csv file into a dataframe
    df = pd.DataFrame(pd.read_csv(f4))
    print(df)
    rsf1 = df.fillna('null')
    print(rsf1)
    rsf2 = pd.DataFrame(rsf1)
    rsf3 = rsf2.drop_duplicates()
    print(rsf3)
    rsf3.to_csv(writefile)
    # -----ONLY FOR CONDITIONS TABLE BLOCK END---------

    # ------calling functions
    file_formatter(f1, wf1)
    file_formatter(f2, wf2)
    file_formatter(f3, wf3)
    file_condit(f4, wf4)
