import torch
import numpy as np

#Directly from data
data = [
    [1, 2],
    [3, 4]
]
x_data = torch.tensor(data)

#From a NumPy array
data = np.array(data)
x_np = torch.from_numpy(data)

#From another tensor
x_ones = torch.ones_like(x_data)
x_rand = torch.rand_like(x_data, dtype=torch.float32)
print(x_rand)

#With random or constant values
shape = (2, 3, )
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

#Attributes of a Tensor
tensor = torch.rand(3, 4)

# We move our tensor to the GPU if available
if torch.cuda.is_available():
    tensor = tensor.to("cuda")
    print(tensor.device)

#Standard numpy-like indexing and slicing
tensor = torch.ones(4, 4)
tensor = torch.cat([tensor, tensor, tensor], dim=1)  # Joining tensors
print(tensor.shape)

#Arithmetic operations
# This computes the matrix multiplication between two tensors. y1, y2, y3 will have the same value
y1 = tensor @ tensor.T
y2 = tensor.matmul(tensor.T)

y3 = torch.rand_like(tensor)
torch.matmul(tensor, tensor.T, out=y3)


# This computes the element-wise product. z1, z2, z3 will have the same value
z1 = tensor * tensor
z2 = tensor.mul(tensor)

z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)

#Single-element tensors
agg = tensor.sum()
agg_item = agg.item()
print(agg_item, type(agg_item))

#In-place operations
print(tensor, "\n")
tensor.add_(5)
print(tensor)

#Bridge with NumPy
#Tensor to NumPy array
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

#A change in the tensor reflects in the NumPy array.
t.add_(1)
print(f"t: {t}")
print(f"n: {n}")

#NumPy array to Tensor
n = np.ones(5)
t = torch.from_numpy(n)

np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")