import pandas as pd
data = pd.read_csv("Files\info.csv")
print(data.head())  # By default it returns the first 5 rows
print(data.tail())  # By default it returns the last 5 rows
print(data.info())

data = data.set_index("学号")
# Or: data.set_index("学号", inplace = True)
# The inplace=True argument specifies that
# the change will be applied to our DataFrame,
# without the need to assign it to a new DataFrame variable.

print(data.head())

data = data.drop("平均学分绩", axis=1)
#As set_index, data.drop("平均学分绩", axis=1, inplace = True) is identical
print(data.head())
