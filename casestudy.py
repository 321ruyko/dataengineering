import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1. Load the dataset:
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang','oldpeak', 'slope', 'ca', 'thal', 'target']
data = pd.read_csv(url, names=columns)
print(data.head())
#2.Data Cleaning
print('*'*100)
print('Data Cleaning:')
for column in data.columns:
    data[column] = pd.to_numeric(data[column], errors='coerce')
data=data.dropna()
print(data.head())
#cleaning cp
valid_values = [0, 1, 2, 3]
data = data[data['cp'].isin(valid_values)]
#cleaning target
valid_target = [0, 1]
data = data[data['target'].isin(valid_target)]
print(data)
#3. Descriptive Statistics:
print('*'*100)
print('Descriptive Statistics:')
print(data.describe())
#Task 1: Age Distribution
male_ages=data[data['sex'] == 1]['age']
female_ages = data[data['sex'] == 0]['age']
plt.hist(male_ages, bins=20, color='red', edgecolor='black',label='Male')
plt.hist(female_ages, bins=20, color='green', edgecolor='black',label='Female')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')
plt.legend(title='Sex')
plt.show()
plt.savefig('task1.png')
#Task2:Gender Distribution
plt.figure(figsize=(8, 6))
# data['sex'] = data['sex'].map({0: 'Female', 1: 'Male'})
g_count=data['sex'].value_counts()
sns.barplot(x=g_count.index,y=g_count.values, palette='viridis' )
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender')
plt.xticks(ticks=[0, 1], labels=['Female', 'Male'])
plt.show()
plt.savefig('task2.png')
#Task3:Chest Pain Type vs. Heart Disease
plt.figure(figsize=(10, 6))
sns.countplot(x='cp', hue='target', data=data, palette={0: "green", 1: "red"})
plt.xlabel('Chest Pain Type (cp)')
plt.ylabel('Count')
plt.title('Relationship between Chest Pain Type and Heart Disease')
plt.legend(title='Heart Disease', labels=['No', 'Yes'])
plt.show()
plt.savefig('task3.png')
#Task4:Cholesterol Levels
sns.boxplot(x='target', y='chol', data=data, palette='Set2')
plt.xlabel('Presence of Heart Disease')
plt.ylabel('Cholesterol Levels (chol)')
plt.title('Distribution of Cholesterol Levels for Patients with and without Heart Disease')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
plt.show()
plt.savefig('task4.png')
#Task5:Pair Plot
# data['target'] = data['target'].map({0: 'No', 1: 'Yes'})
variables = ['age', 'trestbps', 'chol', 'thalach', 'target']
sns.pairplot(data[variables], hue='target', palette='husl')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
plt.show()
plt.savefig('task5.png')
#Task6:Correlation Heatmap
corr=data.corr()
plt.figure(figsize=(12, 8))
print(corr)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
plt.savefig('task6.png')
#Task7:Exercise Induced Angina vs. Maximum Heart Rate
exang = data['exang']
thalach = data['thalach']
target = data['target']
plt.figure(figsize=(8, 6))
plt.scatter(exang[target == 1], thalach[target == 1], color='red', alpha=0.5, label='Heart Disease')
plt.scatter(exang[target == 0], thalach[target == 0], color='blue', alpha=0.5, label='No Heart Disease')
plt.xlabel('Exercise-induced Angina (exang)')
plt.ylabel('Maximum Heart Rate (thalach)')
plt.title('Relationship between Exang and Thalach')
plt.legend()
plt.show()
plt.savefig('task7.png')

