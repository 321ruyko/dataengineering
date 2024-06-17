import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
card_approval_data=pd.read_csv('creditcarddataset.csv')
sns.histplot(data=card_approval_data,hue='Gender',kde=True,x='Age')
plt.show()