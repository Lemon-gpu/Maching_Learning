import pandas as pd
data = {
    "age": [12, 45],
    "height": [189, 187],
    "weight": ["70", "50"]
}
hobby ={
    "hobby":["one","two"]
}

data = pd.DataFrame(data)
data["hobby"] = pd.DataFrame(hobby).values
# https://blog.csdn.net/S_o_l_o_n/article/details/90383176
print(data.describe())