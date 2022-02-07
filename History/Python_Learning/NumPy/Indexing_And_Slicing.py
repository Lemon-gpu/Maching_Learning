import numpy as np
x = np.arange(0,81)
x = x.reshape(9,9)
print(x[1:6:2])#start:stop:step
print(x[6,6])
print(x[1:6:2,2:4:2])

