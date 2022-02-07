import Empirical_Entropy
import pandas as pd
import Information_Gain


def build_C45(dataset: pd.DataFrame, label_index: int):
    if dataset.iloc[:, label_index].drop_duplicates().shape[0] == 1:
        return dataset.iloc[0, label_index]

    if dataset.iloc[:, :label_index].shape[1] == 1:
        return dataset.iloc[label_index].value_counts().index[0]

    features = dataset.columns[:label_index]
    current_best_feature = Information_Gain.calculate_all_infomation_gain_ratio(
        dataset, label_index)[0][0]
    feature_count, total_count = Empirical_Entropy.get_unique_labels_and_count(
        dataset, current_best_feature)
    result_tree = {current_best_feature: {}}
    for i in feature_count:
        new_dataset = dataset[dataset[current_best_feature] == i]
        new_dataset = new_dataset.drop(current_best_feature, 1)
        result_tree[current_best_feature][i] = build_C45(
            new_dataset, label_index)

    return result_tree


data = Empirical_Entropy.create_dataset()
print(data)
print(build_C45(data, -1))
