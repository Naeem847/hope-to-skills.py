from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import(accuracy_score,
             confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score,confusion_matrix,
               classification_report,roc_curve, auc)
import matplotlib.pyplot as plt
import pandas as pd
# step 1:load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# step 2:convert to binary classification(class 0 vs others)
y_binary = (y == 0).astype(int)
# step 3:Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.3, random_state=42)
# step 4:Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test= scaler.transform(X_test)
# step 5:Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)
# step 6:Make predictions
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]  # probability estimates for the positive class
# step 7:Evaluate usinng various metrics
print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print("Classification Report:")
print(classification_report(y_test, y_pred))
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_proba)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)
print("ROC AUC:", roc_auc)

