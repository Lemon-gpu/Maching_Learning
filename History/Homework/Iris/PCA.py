from sklearn.decomposition import PCA
from sklearn import datasets

data = datasets.load_iris().data
target = datasets.load_iris().target

print(target)

pca = PCA(n_components = 'mle', svd_solver = 'full')

new_data = pca.fit_transform(data)
print(new_data)
