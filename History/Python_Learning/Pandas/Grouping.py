import pandas as pd
data = pd.read_csv("Files\info.csv")
print(data.groupby("OS")["Java"].mean())