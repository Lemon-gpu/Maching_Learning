from typing import Tuple
from numpy.lib.function_base import diff
from itertools import combinations

from pandas.core.frame import DataFrame
import Apriori
import pandas as pd
import numpy as np


def difference_of_set(all: list, target: list):
    temp = {}
    for i in all:
        temp[i] = 0
    for j in target:
        temp[j] = 1

    result = []
    for i in temp:
        if temp[i] == 0:
            result.append(i)

    return result


def satisfy(a: list, b: list):
    if len(a) != len(b):
        return False

    for i in range(0, len(a)):
        temp_a: list = a[i]
        temp_a.sort()
        for j in range(0, len(b)):
            temp_b: list = b[j]
            temp_b.sort()

            if temp_a == temp_b:
                return False

    return True


def duplicate(all: list, target: list) -> bool:
    for i in all:
        if i == target:
            return True
        if not satisfy(i, target):
            return True

    return False


def generate_all_subset(target: list):
    result = []
    for i in range(1, len(target)):  # 生成次数
        temp = list(combinations(target, i))
        for j in temp:
            part_1 = list(j)
            part_2 = difference_of_set(target, part_1)
            if not duplicate(result, [part_1, part_2]):
                result.append([part_1, part_2])

    return result


def association_rules_generator(data: pd.DataFrame, itemset: list, min_confidence: int):
    result = []
    count = 1
    for i in itemset:
        for pair in i:
            sub = generate_all_subset(pair[0])
            for k in sub:
                confi = Apriori.confidence(k[0], k[1], data)*100
                flag = "False"
                if confi > min_confidence:
                    flag = "True"
                temp = [str(count), str(pair[0]), str(k[0]), str(confi)+"%",
                        str(Apriori.support(k[0], data)*100)+"%", str(k[0])+"->"+str(k[1]), flag]
                result.append(temp)
                count += 1

                confi = Apriori.confidence(k[1], k[0], data)*100
                flag = "False"
                if confi > min_confidence:
                    flag = "True"
                temp = [str(count), str(pair[0]), str(k[1]), str(confi)+"%",
                        str(Apriori.support(k[1], data)*100)+"%", str(k[1])+"->"+str(k[0]), flag]
                result.append(temp)
                count += 1
    return pd.DataFrame(result, columns=["序号", "I_k", "X_(m-1)", "confidence", "support", "规则", "是否是强规则"])


def frequency_and_rules(filePath: str, min_sup: int, min_confidence: int) -> Tuple[pd.DataFrame, list, pd.DataFrame]:
    data, min_support = Apriori.load_data(filePath, min_sup)
    itemset = Apriori.getting_maximins_frequent_itemset(
        filePath, min_sup)
    result = association_rules_generator(data, itemset, min_confidence)
    return data, itemset, result
