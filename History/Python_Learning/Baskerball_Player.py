import numpy as np
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
players = np.array(players)
mean = players.mean()
std = players.std()
max = mean + std
min = mean - std
count = 0
for i in players:
    if i <= max and i >= min:
        count +=1
print(count)
