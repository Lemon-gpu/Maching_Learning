from sklearn.preprocessing import StandardScaler
X = [[0, 15],
     [1, -10]]
# scale data according to computed scaling values
print(StandardScaler().fit(X).transform(X))
