from typing import ItemsView, List, Tuple
import math
import pandas as pd


def support(target: list, data: pd.DataFrame) -> float:
    count = 0
    for i in range(0, data.shape[0]):
        if searching(data.iloc[i, :], target):
            count += 1
    return count / data.shape[0]


def confidence(antecedent: list, consequent: list, data: pd.DataFrame) -> float:
    union = unioning(antecedent, consequent)
    return support(union, data) / support(antecedent,data)


def load_data(filePath: str, min_support: int) -> Tuple[pd.DataFrame, int]:
    data = pd.read_csv(filePath)
    name = []
    for i in range(0, data.shape[1]):
        name.append("Item "+str(i+1))
    data = pd.read_csv(filePath, names=name, dtype=str)
    return data, math.ceil(data.shape[0]*(min_support / 100))


def clean_data(data: pd.DataFrame, min_support: int) -> pd.DataFrame:
    frequency = {}
    for i in range(0, data.shape[0]):
        for j in range(0, data.shape[1]):
            temp = str(data.iloc[i, j])
            if temp == "nan":
                continue
            if not (temp in frequency):
                frequency[temp] = 1
            else:
                frequency[temp] += 1

    frequency = list(frequency.items())
    temp = []
    for i in frequency:
        i = list(i)
        temp.append(i)
    frequency = sorted(temp, key=lambda x: x[1], reverse=True)
    while True:
        if frequency[len(frequency) - 1][1] < min_support:
            frequency.pop(len(frequency) - 1)
        else:
            break
    return frequency


def unioning(first: List, second: List) -> List:
    result = {}
    for i in first:
        result[i] = 1
    for j in second:
        result[j] = 1
    result = result.keys()
    return list(result)


def corresponding(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    a.sort()
    b.sort()
    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False
    return True


def driver_of_corresponding(target: list, group: list):
    for i in group:
        if corresponding(target, i[0]):
            return False
    return True


def pairing(item_set: pd.DataFrame) -> List:
    result = []
    for i in range(0, item_set.shape[0]):
        for j in range(i + 1, item_set.shape[0]):
            first = item_set.iloc[i, 0]
            second = item_set.iloc[j, 0]
            union = unioning(first, second)
            if len(union) == (len(first) + 1) and driver_of_corresponding(union, result):
               result.append([union, 0])
    return result


def searching(row: pd.Series, target: list) -> bool:
    temp = {}
    for i in target:
        temp[i] = 0

    for i in range(0, row.shape[0]):
        if str(row.iloc[i]) in temp:
            temp[str(row.iloc[i])] = 1

    for i in temp:
        if temp[i] == 0:
            return False

    return True


def digging_frequent_itemset(item_set: pd.DataFrame, data: pd.DataFrame, min_support: int) -> list:

    if item_set.shape[0] == 0:
        return []

    new_item_set = pairing(item_set)
    curr_result = []

    for i in new_item_set:
        for row in range(0, data.shape[0]):
            if searching(data.iloc[row, :], i[0]):
               i[1] += 1

        if i[1] >= min_support:
            curr_result.append(i)

    if len(curr_result) == 1:
        return [curr_result]

    temp_result = digging_frequent_itemset(
        pd.DataFrame(curr_result), data, min_support)
    temp_result.insert(0, curr_result)
    return temp_result


def getting_frequent_itemset(filePath: str, min_sup: int):
    data, min_support = load_data(filePath, min_sup)
    item_set = clean_data(data, min_support)
    result = digging_frequent_itemset(
        pd.DataFrame(item_set), data, min_support)
    result.insert(0, item_set)
    return result


def getting_maximins_frequent_itemset(filePath: str, min_support: int):
    temp_result = getting_frequent_itemset(filePath, min_support)
    temp_result.reverse()
    result = [temp_result[0]]
    for i in range(1, len(temp_result)):
        temp = []
        for a in temp_result[i]:
            flag = False
            for b in temp_result[i-1]:
                if searching(pd.Series(b[0]), a[0]):
                    flag = True
                    break
            if not flag:
                temp.append(a)
        if len(temp) > 0:
            result.append(temp)

    return result
