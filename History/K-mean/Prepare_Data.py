import pandas as pd
import numpy as np
import math


def create_dataset():
    dataSet = [
        [1, 1, -1],  # 数据集
        [2, 1, -1],
        [1, 2, -1],
        [2, 2, -1],
        [4, 3, -1],
        [5, 3, -1],
        [4, 4, -1],
        [5, 4, -1],
    ]
    result = pd.DataFrame(dataSet)
    result.columns = ["feature_1", "feature_2", "belong_to"]
    return result


def distance_compute(target: pd.Series, point: pd.Series) -> float:
    result: float = 0
    for i in range(0, point.shape[0]):
        result += math.pow(target.iloc[i] - point.iloc[i], 2)
    return result


def one_the_nearest(target: pd.Series, points: pd.DataFrame) -> int:
    belong_point = 0
    min_distance = 9999999.99999
    for i in range(0, points.shape[0]):
        curr_distance = distance_compute(target, points.iloc[i, :])
        if curr_distance < min_distance:
            min_distance = curr_distance
            belong_point = i
    return belong_point




def cal_new_point(target: pd.DataFrame) -> pd.Series:
    list = []
    for i in range(0, target.shape[1] - 1):
        temp = 0
        for j in range(0, target.shape[0]):
            temp += target.iloc[j, i]
        temp /= target.shape[0]
        list.append(temp)

    return pd.Series(list)
    
def all_the_nearest(target: pd.DataFrame, points: pd.DataFrame) -> pd.DataFrame:
    result = target
    for i in range(0, target.shape[0]):
        belonging = one_the_nearest(target.iloc[i, :], points)
        result.iloc[i, (target.shape[1] - 1)] = belonging

    return target


def new_points(target: pd.DataFrame, points: pd.DataFrame) -> pd.DataFrame:
    result = []
    for i in range(0, points.shape[0]):
        result.append(cal_new_point(target[target["belong_to"] == i]))

    return pd.DataFrame(result)


def k_mean(target: pd.DataFrame, k: int) -> pd.DataFrame:
    points = []
    for i in range(0, k):
        points.append(target.iloc[i,:])
    points = pd.DataFrame(points)
    for i in range(0, 10):
        target = all_the_nearest(target, points)
        points = new_points(target, points)
    
    return target

print(create_dataset())
print(k_mean(create_dataset(), 2))

