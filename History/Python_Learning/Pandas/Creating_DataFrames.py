import pandas as pd
data = {
    "age": [14, 18, 24, 42],
    "height": [165, 180, 52, 184]
}
data = pd.DataFrame(data,index=["a","b","c","d"])
print(data.loc["a"])
