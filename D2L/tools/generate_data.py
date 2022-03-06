import random
from typing import Tuple
import torch
def synthetic_data(w, b, num_example) -> Tuple[torch.Tensor, torch.Tensor]:
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
