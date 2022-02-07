import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Files/ca-covid.csv")
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format="%d.%m.%y")
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)

df[df["month"]==12][["cases", "deaths"]].plot(kind="area", stacked=False)
plt.show()

df[df["month"]==6][["cases", "deaths"]].plot(kind="scatter", x='cases', y='deaths')
plt.show()

df.groupby('month')['cases'].sum().plot(kind="pie")
plt.show()