import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
titanic_df = pd.read_csv('titanic.csv')
data = titanic_df.dropna(subset=['Age'])
plt.figure(figsize=(10, 6))
g = sns.scatterplot(data=data,x="Age", y='Survived',hue='Survived', palette='coolwarm', alpha=0.6)
plt.title('Scatter Plot of Age vs. Survival')
plt.xlabel('Age')
plt.ylabel('Survived')
plt.yticks([0, 1], ['Not Survived', 'Survived'])
# grouped_data = data.groupby(['Age', 'Pclass', 'Sex'], as_index=False)['Survived'].mean()
# sns.barplot(data=grouped_data, x='Age', y='Survived', hue='Sex', palette='coolwarm')
# plt.title('Survival Rate by Age, Class, and Gender')
# plt.xlabel('Age')
# plt.ylabel('Survival Rate')
# plt.legend(title='Gender', loc='upper right')
# plt.savefig('survival_rate_bar_chart.png')
plt.show()
