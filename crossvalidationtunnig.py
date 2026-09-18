from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold,GridSearchCV,train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import  classification_report
import numpy as np
# load the datasets
iris = load_iris()
X, y = iris.data, iris.target
# initialize the model
model=LogisticRegression(max_iter=200)
# initialize the KFold cross-validator
kf=KFold(n_splits=5, shuffle=True, random_state=42)
fold=1
all_reports=[]
for train_index,test_index in kf.split(X):
    X_train,X_test=X[train_index],X[test_index]
    y_train,y_test=y[train_index],y[test_index]

# train the model
    model.fit(X_train,y_train)
# predict on the test set
    y_pred=model.predict(X_test)
# Generate and print classification report for the current report
    report=classification_report(y_test,y_pred,target_names=iris.target_names,output_dict=True)
    all_reports.append(report)
    fold+=1
# load data
X,y=load_iris(return_X_y=True)
# split data into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
# define model and parameter grid
model=RandomForestClassifier()

# define the model and hyperparameter grid
param_grid = {
    'n_estimators': [10,50, 100],
    'max_depth': [None, 3, 5],
    'criterion': ['gini', 'entropy']
}
# grid search with cross-validation
grid_search = GridSearchCV(model,param_grid, cv=5)
grid_search.fit(X_train,y_train)
# evaluate the best model on the test set
print("Best parameters:", grid_search.best_params_)
y_pred = grid_search.predict(X_test)
print("Classification Report for Best Model:")
print(classification_report(y_test, y_pred))
from sklearn.model_selection import RandomizedSearchCV
# define the model and hyperparameter distribution
import numpy as np
# Define parameter distribution for RandommozedsearchCV
random_search=RandomizedSearchCV(model, param_distributions=param_grid, n_iter=10, cv=5, random_state=42)
random_search.fit(X_train,y_train)
# evaluate the best model on the test set
print("best parameters:", random_search.best_params_)
y_pred=random_search.predict(X_test)
print("Classification Report(y_test,y_pred):")
print(classification_report(y_test, y_pred))