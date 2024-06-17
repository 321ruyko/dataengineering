import pandas as pd
mtcars=pd.read_csv('mtcars.csv')
mtcars.columns=['MPG','CYL','DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']
print(mtcars.head())
print(mtcars.tail())
#creating frequency distribution
fd = mtcars.WT.value_counts(ascending=False)
print(fd)

print("Any random 10 values from the dataset")
print(mtcars.sample(n=10))
print("5% random values from the dataset")
print(mtcars.sample(frac=0.05))



#Replace a particular string within the columns of data set
mtcars.columns = mtcars.columns.str.replace('DRAT', 'DT')
print(mtcars.columns)

mtcars.set_index("MPG",inplace=True)
print(mtcars.head())
print(mtcars.columns)
mtcars.reset_index(inplace=True)
print(mtcars.head())
print(mtcars.columns)

mtcars.drop('MPG',axis=1,inplace=True)
print(mtcars.columns)
mtcars.drop('HP',axis="columns",inplace=True)
print(mtcars.columns)

mtcars.drop(0,axis=0,inplace=True)
print(mtcars.head())

mtcars.drop(1,axis="index",inplace=True)
print(mtcars.head())

print(mtcars.head())

mtcars.sort_values("WT",ascending=False,inplace=True)
print(mtcars.head())
mtcars.WT

print(mtcars.head())
