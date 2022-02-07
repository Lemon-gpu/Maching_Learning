import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Files\ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)

df[df["month"]==6]["cases"].plot(kind = "box")
plt.show()
df[df["month"]==6]["cases"].plot(kind = "hist")
plt.show()