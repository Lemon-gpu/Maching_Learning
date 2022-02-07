from typing import Tuple
import pandas as pd
import math

# 这个函数主要是为了创造一下数据集
def create_dataset() -> pd.DataFrame:
    '''
    dataSet = [
        [0, 0, 0, 0, 'no'],  # 数据集
        [0, 0, 0, 1, 'no'],
        [0, 1, 0, 1, 'yes'],
        [0, 1, 1, 0, 'yes'],
        [0, 0, 0, 0, 'no'],
        [1, 0, 0, 0, 'no'],
        [1, 0, 0, 1, 'no'],
        [1, 1, 1, 1, 'yes'],
        [1, 0, 1, 2, 'yes'],
        [1, 0, 1, 2, 'yes'],
        [2, 0, 1, 2, 'yes'],
        [2, 0, 1, 1, 'yes'],
        [2, 1, 0, 1, 'yes'],
        [2, 1, 0, 2, 'yes'],
        [2, 0, 0, 0, 'no']
    ]
    result = pd.DataFrame(dataSet)
    result.columns = ["age", "work", "house", "credibility", "load"]# 给DataFrame加个列
    return result
    '''
    dataSet = [
        [1, 1, 0, 1],  # 数据集
        [0, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 0, 1],
        [1, 0, 0, 0],
        [1, 0, 1, 0],
    ]
    result = pd.DataFrame(dataSet)
    result.columns = ["gender", "student", "ethnic", "computer"]# 给DataFrame加个列
    return result
    

# 这个函数用来计算一个数据集合里面某一列的东西的出现个数
def get_unique_labels_and_count(dataset: pd.DataFrame, index) -> Tuple[dict, int]:
    raw_data = dataset.loc[:, index]
    raw_labels = raw_data.drop_duplicates().reset_index(drop=True)
    total_number = 0

    labels = {}
    for i in range(0, raw_labels.shape[0]):
        labels[raw_labels[i]] = 0

    for i in range(0, dataset.shape[0]):
        labels[raw_data.iloc[i]] += 1
        total_number += 1
    return labels, total_number

#这个函数用来计算一个数据集里面一列的经验熵
def calculate_empirical_entropy_of_a_column(dataset: pd.DataFrame, index) -> float:
    labels,total_number = get_unique_labels_and_count(dataset, index)
    #print(labels)

    result = 0.0
    for i in labels:
        i_x = labels[i] / total_number
        result += i_x * (-math.log2(i_x))
    return result
