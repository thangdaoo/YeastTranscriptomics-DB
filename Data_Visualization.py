from matplotlib import pyplot as plt
import pandas as pd
#create a list of samples
samples = []
df = pd.read_csv('data/conditions_annotation.csv')
for x in df['ID']:
    #print(x)
    samples.append(x)
#print(df['ID'])
print(samples)

