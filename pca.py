import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# load the iris datasets
iris = load_iris()
# fetures
X = iris.data
# labels
y = iris.target
target_names = iris.target_names
# standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# step 3:apply pca to reduce the dimensionality of the data
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
# step 4: visualize the 2D PCA results
plt.figure(figsize=(8, 6))
colors = ['navy', 'turquoise', 'darkorange']
for color, i, target_name in zip(colors,[0, 1, 2], target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], alpha=0.7, color=color, label=target_name)
plt.legend()
plt.title('2D PCA of Iris Dataset')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
# step 5:explain the variance 
print('Explained variance ratio:', pca.explained_variance_ratio_)