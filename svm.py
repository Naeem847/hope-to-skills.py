import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# load the dataset(update the file path to your local path)
file_path="diabetes.csv"
df=pd.read_csv(file_path)
# display basic information
print("dataset information")
print(df.info())
print("\nfirst 5 rows")
print(df.head())
# checking the missing value
print(df.isnull().sum())
# fill the missing numerical ValueError
df.fillna(df.median(numeric_only=True),inplace=True)
# filling ,missing categorical values with the mode(if any)
for col in df.select_dtypes(include=['object']):
    df[col].fillna(df[col].mode(),[0],inplace=True)
# step 3: prepare data
# separate the fetureb and target variable
X=df.drop(columns=['Outcome'])
y=df['Outcome']
# apply standard scalling
scaler= StandardScaler()
X_scaled=scaler.fit_transform(X)
# step 5:split data into training and testing set
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
# step 6:modified train a support vector machine classifier
from sklearn.svm import SVC
print("\ntraining svm classifier")
svm_model=SVC(kernel='linear',random_state=42)
svm_model.fit(X_train,y_train)
# model evaluation for SVM
y_pred_svm=svm_model.predict(X_test)
# calculate acuracy
svm_accuracy=accuracy_score(y_test,y_pred_svm)

print(f"\nSVM model sccuracy:{svm_accuracy:.2f}")
# classification report
print("\nclassification report")
print(classification_report(y_test,y_pred_svm))
# confusion matrix
print("\nconfusion matrix")
print(confusion_matrix(y_test,y_pred_svm))
print(confusion_matrix(y_test,y_pred_svm))