import Empirical_Entropy
import pandas as pd

# 计算条件变量……但似乎没啥用。主要就是在data_index发生的前提下，labels_index发生的概率，但说实话这个函数有点太过了，纯纯的摆烂了


def calculate_conditional_probability(dataset: pd.DataFrame, data_index, labels_index) -> list:
    raw_data = dataset.loc[:, data_index]
    result = {}

    raw_data = list(raw_data.unique())
    raw_labels = list(dataset.loc[:, labels_index].unique())

    for i in raw_data:
        result[i] = []
        specific_labels = dataset[dataset[data_index]
                                  == i].loc[:, labels_index]
        encode_labels, total_number = Empirical_Entropy.get_unique_labels_and_count(
            pd.DataFrame(specific_labels))
        for j in encode_labels:
            result[i].append(encode_labels[j]/total_number)

    result = pd.DataFrame(result)

    result.columns = raw_data
    result.loc[:, result.shape[1]] = raw_labels
    result = result.set_index(result.shape[1]-1)

    return result.transpose()

#计算条件经验熵，数据集，在什么条件下，什么事件的条件经验熵


def empirical_conditional_entropy(dataset: pd.DataFrame, data_index, label_index) -> float:
    pi, total_number = Empirical_Entropy.get_unique_labels_and_count(
        dataset, data_index)
    result = 0
    for i in pi:
        pi[i] = pi[i] / total_number
        result += (pi[i] * Empirical_Entropy.calculate_empirical_entropy_of_a_column(
            (dataset[dataset[data_index] == i]), label_index))
    return result

#计算信息增益


def calculate_information_gain(dataset: pd.DataFrame, data_index, label_index) -> float:
    empirical_entropy = Empirical_Entropy.calculate_empirical_entropy_of_a_column(
        dataset, label_index)
    empirical_conditional_entropy_value = empirical_conditional_entropy(
        dataset, data_index, label_index)
    return empirical_entropy-empirical_conditional_entropy_value

#计算最优特征


def best_feature(dataset: pd.DataFrame, label_index):
    max_index = 0
    max_value = -1
    columns = dataset.columns

    for i in range(0, dataset.shape[1]-1):
        current_gain = calculate_information_gain(
            dataset, columns[i], label_index)
        if current_gain > max_value:
            max_index = i
            max_value = current_gain
    return dataset.columns[max_index]


def calculate_all_infomation_gain(dataset: pd.DataFrame, label_index:int):
    columns = dataset.columns[:-1]
    result = {}
    for i in columns:
        result[i] = calculate_information_gain(dataset, i, dataset.columns[label_index])
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return result
