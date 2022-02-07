import numpy as np
import pandas as pd
import math


def create_dataset():# Create a simple data to test
    data = {
        "fight": [1, 5, 108, 115],
        "kiss": [101, 89, 5, 8],
        "classification": ["romance", "romance", "action", "action"]
    }
    return pd.DataFrame(data)


def distance_compute(target: pd.Series, data: pd.Series) -> int:
    '''
    Parameters:
        target: test set
        dataset: train set
        k:
    '''
    result: float = 0 #存放最终结果
    index: int = len(target)-1 # 表示要计算的分量总数
    for i in range(0, index): # 算欧氏距离
        result += math.pow(target.iloc[i]-data.iloc[i], 2)#计算每个分量的差的平方
    return math.sqrt(result) #开方


def single_classification(target: pd.Series, dataset: pd.DataFrame, k: int) -> str: #对于一条数据而言
    #init
    result: list = []
    classification: pd.DataFrame = pd.DataFrame(
        dataset.iloc[:, -1].drop_duplicates())
    classification.loc[:, 1] = 0

    #Step 1: 计算距离
    for j in range(0, dataset.shape[0]):  # row
        distance = distance_compute(target, dataset.iloc[j, :])
        temp_tuple = (distance, dataset.iloc[j, -1])
        result.append(temp_tuple)
    result.sort(key=(lambda x: x[0]))

    #Step 2: 计算前k个的频率
    for i in range(0, k):
        temp = result[i]
        classification.loc[classification.iloc[:,0] == temp[1], 1] += 1

    #Step 3: 返回频率最大那个
    max_index = 0
    for i in range(0, classification.shape[0]):
        if classification.iloc[i, 1] > classification.iloc[max_index, 1]:
            max_index = i
    return classification.iloc[max_index, 0]


def classification(target: pd.DataFrame, dataset: pd.DataFrame, k: int) -> str: #对于整个测试集而言
    error = 0
    for i in range(0, target.shape[0]):
        result = single_classification(target.iloc[i, :], dataset, k)
        print("prediction: "+str(result)+" actually: "+str(target.iloc[i, -1]))
        if result != target.iloc[i, -1]:
            error += 1

    print("error: " + str(error/target.shape[0]))


def test():
    classification(
        target=pd.DataFrame({"fight": [101, 5], "kiss": [
                            20, 50], "classification": ["action", "romance"]}),
        dataset=create_dataset(),
        k=3
    )
