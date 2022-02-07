from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
X = [[ 1,  2,  3],  # 2 samples, 3 features
     [11, 12, 13]]
y = [0, 1]  # classes of each sample
clf.fit(X, y)
print(clf.predict(X))  # predict classes of the training data
print(clf.predict([[4, 5, 6], [14, 15, 16]]))  # predict classes of new data