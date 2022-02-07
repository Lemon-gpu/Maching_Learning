import numpy as np
x= np.arange(0,10,1)
print(x)
x = x.reshape(5,2)
print(x)
x = x.reshape(x.size)
print(x)