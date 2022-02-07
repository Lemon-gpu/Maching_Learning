from cProfile import label
from typing import Tuple
import numpy as np
import sklearn.neighbors
import pandas as pd
import os


def load_file(filepath, filename) -> pd.DataFrame:
    array = []
    file = open(filepath+"/"+filename, "r")
    label = int(filename.split("_")[0])
    while True:
        temp = file.read(1)
        if temp != '0' and temp != '1':
            if temp == '':
                break
            #print(temp)
            continue
        temp = int(temp)
        array.append(temp)
    array.append(label)
    result = pd.DataFrame(array).transpose()
    return result


def load_train_set(filepath="K-Nearest_Neighbor/Handwritten_Numeral_Recognition/trainingDigits") -> pd.DataFrame:
    all_filename = os.listdir(filepath)
    result = pd.DataFrame()
    for i in all_filename:
        temp = load_file(filepath, i)
        result = result.append(temp)
    return result


def load_test_set(filepath="K-Nearest_Neighbor/Handwritten_Numeral_Recognition/testDigits") -> pd.DataFrame:
    all_filename = os.listdir(filepath)
    result = pd.DataFrame()
    for i in all_filename:
        temp = load_file(filepath, i)
        result = result.append(temp)
    return result


def feature_label_seperation(data: pd.DataFrame) -> Tuple[np.array, np.array]:
    return data.iloc[:, :-2].to_numpy(), data.iloc[:, -1].to_numpy().ravel()


def KNN_train(train_data: pd.DataFrame):
    features, labels = feature_label_seperation(train_data)
    classifier = sklearn.neighbors.KNeighborsClassifier()
    classifier.fit(features, labels)
    return classifier


def KNN_test(classifier: sklearn.neighbors.KNeighborsClassifier,
             test_data: pd.DataFrame):
    features, labels = feature_label_seperation(test_data)
    error = 0
    for i in range(0, features.shape[0]):
        feature = features[i, :].reshape(1, features.shape[1])
        predition = classifier.predict(feature)[0]
        print("Prediction: " + str(predition) +
              ", Actually: " + str(labels[i]))
        if predition != labels[i]:
            error += 1
    print("Error: "+str(error)+", Error rate:"+str(error/labels.shape[0]))


def main_method():
    train = load_train_set()
    test = load_test_set()
    KNN_test(KNN_train(train), test)


main_method()
