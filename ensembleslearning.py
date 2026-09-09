
""" esembleslearning classification for

 diabetes dataset"""

import pandas as pd

# df=pd.read_csv('ensembles.csv')
# print(df.head(5))
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.svm import SVC
file_path="ensembles.csv"
df=pd.read_csv(file_path)

print(df.head(5))
# display basic infomation
print(df.info())
# handle missing values
print("\nchecking for missing values:")
print(df.isnull().sum())
# fill missing numerical values with the median
df.fillna(df.median(numeric_only=True), inplace=True)
# fill missing categorical values with the mode
df.fillna(df.mode().iloc[0], inplace=True)
for col in df.select_dtypes(include=['object']):
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    #  step 3 prepare the data for training and testing  
    # separate features and target variable
X = df.drop('Outcome', axis=1)
y = df['Outcome']
# step 4:apply standard scaling to the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# step 5: split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
# step 6: train a support vector machine (SVM) classifier

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# Bagging model
Bagging_model = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=3)
Bagging_model.fit(X_train, y_train)
# prediction and acuracy
y_pred_bag= Bagging_model.predict(X_test)
print("Bagging Classifier Accuracy:", accuracy_score(y_test, y_pred_bag))
# accuracy = accuracy_score(y_test, y_pred)
from sklearn.ensemble import AdaBoostClassifier
# AdaBoost model
boosting_model = AdaBoostClassifier(n_estimators=10)
boosting_model.fit(X_train,y_train)
# prediction and acuracy
y_pred_boost=boosting_model.predict(X_test)
print("boosting accuracy:",accuracy_score(y_test,y_pred_boost))
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
# define Bsemodel
base_model = [
    ('tree',DecisionTreeClassifier()),
    ('svm',SVC(probability=True)),
]
# meta model is logistic regression
stacking_model = StackingClassifier(estimators=base_model, final_estimator=LogisticRegression())
stacking_model.fit(X_train,y_train)
# prediction and acuracy
y_pred_stack=stacking_model.predict(X_test)
print("stacking accuracy:",accuracy_score(y_test,y_pred_stack))


