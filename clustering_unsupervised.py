from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# load the iris datasets

iris=load_iris()
X=iris.data
Y =iris.target
# create a data frame a better visualization
df=pd.DataFrame(data=X,columns=iris.feature_names)
df['actual_label']=Y
# applying kmeans clustering
k=3
kmeans=KMeans(n_clusters=k ,random_state=42)
df['cluster_label']=kmeans.fit_predict(X)
# compare actual vs cluster labels
# sns.pairplot(df,hue='actual_label',palette='Set1')
# plt.subtitle('Actual Labels')
# sns.pairplot(df,hue='cluster_label',palette='Set2')
# plt.show()
# optional:visualize clustering in 2D using PCA
plt.figure(figsize=(8,6))
sns.scatterplot(x=X[:,0],y=X[:,1],hue=df['cluster_label'],palette='viridis', s=100)
centers=kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c='red',s=200,marker='X',label='Centroids')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('KMeans Clustering (2 features)')
plt.legend()
plt.grid(True)
plt.show()
print(plt.show())