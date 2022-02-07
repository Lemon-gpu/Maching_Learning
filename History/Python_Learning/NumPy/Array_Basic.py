import numpy as np
print("\nOne dimension variable x")
x = np.array([1, 2, 3, 7, 8, 9, 4, 5])
# NumPy arrays are homogeneous,
# meaning they can contain only a single data type,
# while lists can contain multiple different types of data.
print(x)
print("Append element")
x = np.append(x, 2)
print(x)
print("Delect element")
x = np.delete(x, 4)
print(x)
print("Sort element")
print(np.sort(x))

print("\nTwo dimension variable y")
y = np.array([
    [1, 2, 3],
    [7, 8, 9],
    [4, 5, 6]
])
print(y)
print("Dimension: "+str(y.ndim))
print("Size: "+str(y.size))
print("Shape: "+str(y.shape))
#When axis is specified, values must have the correct shape
print("Append element")
print(np.append(y, [[1, 2, 3]], axis=0))
print(np.append(y, [[1], [2], [3]], axis=1))
print("Delect element")
y = np.append(y, [[1, 2, 3]], axis=0)
print(y)
y = np.delete(y, 3, axis=0)
print(y)

print("Create evenly spaced intervals")
print(np.arange(6,50,6))