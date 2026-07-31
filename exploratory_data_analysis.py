import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import sklearn

import seaborn as sns

import warnings

warnings.filterwarnings('ignore')

plt.rcParams["figure.figsize"]=[10,5]

# ignore warnigs

import warnings

# set the warning filters to ignore futurewarnigs
warnings.simplefilter(action="ignore",category=FutureWarning)


# file_path=('eda_data.csv')

df=pd.read_csv('eda_data.csv')
# display basic information

print(df.info())
print(df.head())
print("total data")
print(df)
print("show the seaborn functionality")
current_palette1=sns.color_palette()
sns.palplot(current_palette1)
print(plt.show())

print("continous coolor palettes")
# current_palette2=sns.color_palette()

sns.palplot(sns.color_palette('colorblind'))
print(plt.show())

# print the colorblind people 
current_palette2=sns.color_palette()

sns.palplot(sns.color_palette('colorblind'))
print(plt.show())

# simple graph
import matplotlib.pyplot as plt
import seaborn as sns
# create figure and axis
plt.figure(figsize=(10,6))
sns.countplot(x='pclass', hue='survived', data=df)
plt.title('survival rate by passenger class')
plt.xlabel('passenger class')
plt.ylabel('count')
plt.legend(labels=['did not survive','survived'])
print(plt.show())
# Survival rate by gender
df=pd.read_csv('eda_data.csv')
import matplotlib.pyplot as plt
import seaborn as sns
# create figure and axis
plt.figure(figsize=(10,6))
sns.countplot(x='sex', hue='survived', data=df)
plt.title('survival rate by Gender')
plt.xlabel('Gender')
plt.ylabel('count')
plt.legend(labels=['did not survive','Survived'])
print(plt.show())
print(df.columns)

#age distribution of passengers
print("age distribution of passengers")
plt.figure(figsize=(12,6))
sns.histplot(data=df,x='age',bins=30,kde=True)
plt.title('Age distribution of passengers')
plt.xlabel('age')
plt.ylabel('count')
plt.axvline(df['age'].mean(),color='red',linestyle='--',label='Mean age')
plt.legend()
print(plt.show())
# maing dynamic graph using plotly and plotly express
import pandas as pd
import plotly.express as px
# 1.Bar chart count of survived  
fig1=px.bar(df,x="survived",title="survived  count",labels={"survived":"survived(0=NO,1=yes)"})
fig1.show()
# 2.histogram age distribution
fig2=px.histogram(df,x="age",nbins=30,title="age distribution of passengers",labels={"age":"age"})
print(fig2.show())
