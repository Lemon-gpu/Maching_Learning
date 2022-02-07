import numpy as mp
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("Decision_tree\Lenses\lenses.data")
data = data.drop("index", 1)
features = data.iloc[:,:-1]
labels = data.iloc[:,-1]

features_train, features_test, labels_train, labels_test = train_test_split(features.to_numpy(),labels.to_numpy().ravel())

print(features_train)
print()
print(features_test)
print()
print(labels_test)
print()
print(labels_train)
print()

dtc = DecisionTreeClassifier()

dtc.fit(features_train,labels_train.T)

label_predict = dtc.predict(features_test)
print(label_predict)