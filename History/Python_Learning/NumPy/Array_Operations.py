import numpy as np
x = np.arange(0,9)
print(x.sum())
print(x.reshape(3,3).T*2)

x = np.array([14, 18, 19, 24, 26, 33, 42, 55, 67])

print(np.mean(x))
print(np.median(x))
print(np.var(x))
print(np.std(x))