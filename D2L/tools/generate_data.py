import random
from typing import Tuple
from torch.utils import data
import torch
def synthetic_data(w: torch.Tensor, b: torch.Tensor, num_example: int) -> Tuple[torch.Tensor, torch.Tensor]:
    X: torch.Tensor = torch.normal(0, 1, (num_example, len(w)))
    y: torch.Tensor = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1)) #-1意味着自动计算的属性，这里意味着我只要一列，行数随意

def data_iter(batch_size: int, features: torch.Tensor, labels: torch.Tensor):
    num_example = len(features)
    indices = list(range(0, num_example))
    random.shuffle(indices)
    for i in range(0, num_example, batch_size):
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_example)]
        )
        yield features[batch_indices], labels[batch_indices] #可迭代的对象，状态维持此刻

def load_array(data_arrays: tuple, batch_size: int, is_shuffle = True):
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle = is_shuffle)

def gen_weight_bias_matrix(features: int, labels: int) -> Tuple[torch.Tensor, torch.Tensor]:
    W = torch.normal(0, 1, (features, labels), requires_grad=True)
    b = torch.normal(0, 0.01, labels, requires_grad=True)

    return W, b

