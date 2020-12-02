import pandas as pd
import numpy as np

dataframe = pd.read_excel( 'Finalproject/SeedUnofficialAppleData.xlsx')

dataframe.fillna(' ', inplace = True)
dataframe.columns =['Model', 'Release(d) with OS', 'Date','Discontinued', 'Support Ended', 'Final OS', 'Lifespan Max', 'Lifespan Min', 'Launch Price']

df = dataframe.set_index('Model')

df1 = df.drop('model')
df2 = df1.drop(df1.index[0])
print(df2)