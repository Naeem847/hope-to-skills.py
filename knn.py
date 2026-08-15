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
x=df.drop('terget',axis=1)
y=df['target']
# assuming x and y are defined
X_train,x_test,y_train,y_test=train_test_split(x,y,test)