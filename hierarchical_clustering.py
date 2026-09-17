from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# load the iris datasets
irirs=load_iris()
X=irirs.data
y_true=irirs.target
# create a data frame a better visualization
df=pd.DataFrame(data=X,columns=irirs.feature_names)
df['actual_label']=y_true
# applying hierarchical clustering
# step 1:plot the dendrgram
linked= linkage(X, method='ward')
plt.figure(figsize=(8, 5))
# this line generate the hierarchical clustering dendrogram
# from a linkage matrix ,showing the tree structure of the clusters
# with the most dissimilar clusters separated first oriented top-down 
# and with leaf nodes showing the individual samples
# how many original observation they contains
dendrogram(linked,
           orientation='top',
           distance_sort='descending',
           show_leaf_counts=True
)
plt.title('Hierarchical Clustering Dendrogram(ward linkage)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.grid(True)
plt.show()
# step 2: apply agglomerative clustering
# number of clusters 
k=3  
hc=AgglomerativeClustering(n_clusters=k, metric='euclidean', linkage='ward')
df['cluster_label']=hc.fit_predict(X)
#  step 3: visualize the clustering results
plt.figure(figsize=(6,4))
sns.scatterplot(x=X[:,0],y=X[:,1],hue=df['cluster_label'],palette='Set2', s=100)
plt.xlabel(irirs.feature_names[0])
plt.ylabel(irirs.feature_names[1])
plt.title('Hierarchical Clustering (2 features)')
plt.grid(True)
plt.show()
print(plt.show())