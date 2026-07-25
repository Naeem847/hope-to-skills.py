import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

df=pd.read_csv('D:\object_oriented_programming1.py\hope-to-skills.py\employees_of_software.csv')
print(df)

# select the numeric cols for regression
numeric_cols=df.select_dtypes(include=['int64','float64']).columns.tolist()

# # # numeric_cols.remove('Id')
print(numeric_cols)
# define the features X and terget Y
X=df[['age']]
Y=df['salary']

# split data into training and testing
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)

# create and train the linear regretion model
model=LinearRegression()
model.fit(X_train,Y_train)

# predict on test date

Y_pred=model.predict(X_test)

# plot regression line
plt.scatter(X_test,Y_test,color='blue',label='actual Date')

plt.plot(X_test,Y_pred,color='red',linewidth=2,label='regression')

plt.xlabel("Age")

plt.xlabel("Salary")

plt.title("linear regression: Age Vs salary")
plt.legend()
plt.show()

# Display model coefficients

print("\nmodel coefficient:")

print(f"model intercept:{model.intercept_}")

print(f"slope:{model.coef_[0]}")

# predict foor new data

new_ages=pd.DataFrame({'age':[25,30,35,40,45]})

new_salaries=model.predict(new_ages)

print("predicted salaries for given ages:")

for Age,salary in zip(new_ages['Age'],new_salaries):

    print(f"Age:{Age},predicted salary: {salary:.2f}")
    
