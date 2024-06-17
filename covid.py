# import pandas as pd
# import matplotlib.pyplot as plt
# covid=pd.read_csv('case.csv')
# c=covid.groupby('province')['confirmed'].sum()
# plt.bar(c.index,c.values,color='skyblue')
# plt.xticks(rotation=75)
# plt.xlabel("Provinces")
# plt.ylabel("Total Count")
# plt.title('Covid Positive cases')
# plt.show()
#
#
import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
print(sb.get_dataset_names())
c=sb.load_dataset('tips')
print(c.head())
gap=px.data.gapminder()
print(gap)
sb.relplot(data=c,x="total_bill",y='tip',kind='scatter')
plt.title("Total Bill vs Tip")
plt.show()

