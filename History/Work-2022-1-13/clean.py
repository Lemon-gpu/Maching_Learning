from collections import OrderedDict
import pandas

class ORDER:
    row_first = 1
    column_first = 2

def read_file(path: str = "Work-2022-1-13\CircR2Disease_circRNA-disease associations.xlsx") -> pandas.DataFrame:
    df = pandas.read_excel(path)
    df = df.loc[:,["circRNA Name", "Disease Name"]]
    return df


def get_count_of_circRNA_and_diseases(data: pandas.DataFrame):
    result = []
    for i in range(0, data.shape[1]):
        series = data.iloc[:, i]
        series = series.drop_duplicates()
        result.append(list(series))
    return result[0], result[1]

def search_related_disease(data: pandas.DataFrame, target: str) -> list:
    result = []
    for i in range(0, data.shape[0]):
        row = data.iloc[i, :]
        if row.iloc[0] == target:
            result.append(str(row.iloc[1]))
    return result

def encode_matrix(matrix: pandas.DataFrame):
    new_row_name = []
    for i in range(0, matrix.shape[0]):
        new_row_name.append("C" + str(i))
    matrix.index = new_row_name

    new_column_name = []
    for i in range(0, matrix.shape[1]):
        new_column_name.append("D" + str(i))
    matrix.columns = new_column_name
    
    return matrix

def generate_matrix(data: pandas.DataFrame) -> pandas.DataFrame:
    circRNA, disease = get_count_of_circRNA_and_diseases(data)
    result = pandas.DataFrame(index = circRNA, columns = disease)
    result.loc[:, :] = 0
    for circRNA_name in circRNA:
        related_disease = search_related_disease(data, circRNA_name)
        for disease_name in related_disease:
            result.loc[circRNA_name, disease_name] = 1
    return encode_matrix(result)

def erase_row(matrix: pandas.DataFrame, percentage: float) -> pandas.DataFrame:
    sum_of_each_row: pandas.Series = matrix.apply(lambda x: x.sum(), axis = "columns")
    temp1 = sum_of_each_row.drop_duplicates().sort_values()
    threshhold = temp1.iloc[int(temp1.shape[0] * percentage)]
    for i in range(0, matrix.shape[0]):
        if sum_of_each_row.iloc[i] < threshhold:
            matrix.drop(index = "C" + str(i), inplace = True)
    return matrix

def erase_column(matrix: pandas.DataFrame, percentage: float) -> pandas.DataFrame:
    sum_of_each_column: pandas.Series = matrix.apply(lambda x: x.sum(), axis = "index")
    temp1 = sum_of_each_column.drop_duplicates().sort_values()
    threshhold = temp1.iloc[int(temp1.shape[0] * percentage)]
    for i in range(0, matrix.shape[1]):
        if sum_of_each_column.iloc[i] < threshhold:
            matrix.drop(columns = "D" + str(i), inplace = True)
    return matrix

def erase_under_threshhold(matrix: pandas.DataFrame, percentage: float = 0.25, order: ORDER = ORDER.row_first) -> pandas.DataFrame:
    if percentage == 0:
        return matrix

    if order == ORDER.row_first:
        return erase_column(erase_row(matrix, percentage), percentage)
    else:
        return erase_row(erase_column(matrix, percentage), percentage)

def main_function():
    data = read_file()
    result = generate_matrix(data)
    result.to_excel("result.xlsx", index = True, header = True)
    erase_under_threshhold(pandas.read_excel("result.xlsx", index_col = 0, header = 0)).to_excel("new_result.xlsx", index = True, header = True)

main_function()
