import matplotlib.pyplot as plt
import pandas as pd
s = pd.read_csv("Files\info.csv",encoding="UTF-8")
s = s.sort_values("Ranking",ascending=True)
s = s.drop("Ranking",axis=1)
s = s.drop("ID",axis=1)
s.plot(kind="bar")
plt.show()