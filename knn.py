import pandas as pd
from sklearn import neighbors,datasets
from sklearn.model_selection import train_test_split
iris=datasets.load_iris()
print(type(iris))
#  sklearn.utils._bunch.Bunch
# def __init_(**kwargs):
df=pd.DataFrame(data=iris.data,columns=iris.feature_names)
# add the terget column
df['target']=iris.target
# display the dataframe
print(df.head())
from sklearn.model_selection import train_test_split
x=df.drop('target',axis=1)
y=df['target']
# assuming x and y are defined
X_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# create the model
model=neighbors.KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
# predict on test data
y_pred=model.predict(x_test)
# calculate accuracy
accuracy=accuracy_score(y_test,y_pred)
print(f"model accuracy:{accuracy:.2f}")

# classification report
print("\nclassification_report")
print(classification_report(y_test,y_pred))

# confision matrics
print(confusion_matrix(y_test,y_pred))