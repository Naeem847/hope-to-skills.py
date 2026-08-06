import pandas as pd

df = pd.read_csv("logistics_regrassions.csv")
# df.to_csv("logistics_regrassions.csv")
print(df.head)

from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
# apply label encoding to categorical columns 
categorical_columns = df.select_dtypes(include=['object']).columns  
label_encoders = {}
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le


# from sklearn.preprocessing import standardScaler
# seperate features and target variable
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# applying standard scaling to features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# split datainto training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
# split data(80% training and 20% testing) into training and testing sets

# train a logistic regression model
from sklearn.linear_model import LogisticRegression
# initialize the logistic regression model
model = LogisticRegression()
# train the model
model.fit(X_train, y_train)
# model evaluation
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# predict on test data
y_pred = model.predict(X_test)
# calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"model accuracy: {accuracy:.2f}")
# classification report
print(classification_report(y_test, y_pred))
# confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix(y_test, y_pred))
