import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

dataset = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(
        10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
)

print(dataset.target_transform(dataset.targets))
