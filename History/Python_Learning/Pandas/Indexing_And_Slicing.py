import pandas as pd
data = {
    "age": [12, 45],
    "height": [189, 187],
    "weight": [70, 50]
}
print("\nIndexing")
data = pd.DataFrame(data, index=["Tom", "Tony"])
print(data["age"])  # The result is a Series object.
print("Another data")
print(data[["age", "height"]])  # The result is a DataFrame object.

print("\nSlicing")
# iloc follows the same rules as slicing does with Python lists.
print(data.iloc[1:])

print("\nConditions")
print(data[(data.age >= 45) & (data.height > 180)])
