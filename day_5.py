import pandas as pd
import numpy as np
df =pd.read_csv("income.csv")
print(df.head())
print('>'*82)
# print(df.tail())
# print(df.Index.unique())
# print(pd.crosstab(df.Index,df.State))
# print(df.Index.value_counts(ascending=False))
# print(df.sample(frac=0.05))
sample_data=pd.DataFrame({"var1":np.arange(1,20,2)},index=[9,8,7,6,10,1,2,3,4,5])
print(sample_data)
print(df.describe(include=['object']))
data=df.loc[(df.Index=="A")|(df.Index=="W")]
print(data)

