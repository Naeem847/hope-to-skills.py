
""" esembleslearning classification for

 diabetes dataset"""

import pandas as pd
# df=pd.read_csv('ensembles.csv')
# print(df.head(5))
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
file_path="ensembles.csv"
df=pd.read_csv(file_path)
print(df.head(5))
# display basic infomation
print(df.info())
