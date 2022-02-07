import numpy as np
import pandas as pd
import math

def create_dataset():
    data = {
        "romance": [(1, 101), (5, 89)],
        "action": [(108, 5), (115, 8)]
    }
    return pd.DataFrame(data)


def distance_compute(target: tuple, data: tuple) -> int:
    '''
    Parameters:
        target: test set
        dataset: train set
        k: 
    '''
    result: float = 0
    index: int = len(target)
    for i in range(0, index):
        result += math.pow(target[i]-data[i],2)
    return math.sqrt(result)


def classify_raw_implement(target: tuple, dataset: pd.DataFrame, k: int) -> str:
    result: list = []
    column_name: list = list(dataset)

    for i in range(0, dataset.shape[0]):  # row
        for j in range(0, dataset.shape[1]):  # column
            distance = distance_compute(target, dataset.iloc[i, j])
            temp_tuple = (distance, column_name[j])
            result.append(temp_tuple)
    result.sort(key=(lambda x: x[0]))

    dataset.loc[2] = [0 for i in range(0,len(column_name))]
    for i in range(0, k):
        temp = result[i]
        dataset.loc[2, temp[1]] += 1

    max_index = -1
    for i in range(0,dataset.shape[1]):
        if max_index < dataset.iloc[2, i]:
            max_index = i
    return column_name[max_index]


print(classify_raw_implement((101, 20), create_dataset(), 3))
