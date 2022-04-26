from typing import Tuple
from sympy import im
import torch
import torch.utils.data as data

import torchvision.datasets as datasets
import torchvision.transforms as tf

import numpy as np
import tools.plot as plot

def load_data_Fashion_MNIST(batch_size: int, resize = None) -> Tuple[data.DataLoader, data.DataLoader]:
    transform_pipeline = [] 

    if resize is not None:
        transform_pipeline.append(tf.Resize(resize)) # 将图像缩放到指定大小
    transform_pipeline.append(tf.ToTensor()) 

    transforms = tf.Compose(transform_pipeline) # 将transformer管线组合成一个transformer

    mnist_train = datasets.FashionMNIST(
        root = "./data", train = True, download = True, transform = transforms
    )
    mnist_test = datasets.FashionMNIST(
        root = "./data", train = False, download = True, transform = transforms
    )

    train_loader = data.DataLoader(
        dataset = mnist_train, batch_size = batch_size, shuffle = True, num_workers = get_dataloader_workers()
    )

    test_loader = data.DataLoader(
        dataset = mnist_test, batch_size = batch_size, shuffle = False, num_workers = get_dataloader_workers()
    ) 

    return train_loader, test_loader 


def get_fashion_mnist_labels(labels : torch.Tensor) -> torch.Tensor:
    text_labels = [
        "t-shirt", "trouser", "pullover", "dress", "coat", "sandal", "shirt", "sneaker", "bag", "ankle boot"
    ]
    return [text_labels[int(i)] for i in labels] 

def show_images(images: torch.Tensor, num_rows: int, num_cols: int, titles = None, scale = 1.5) -> None:
    figs = (num_cols * scale, num_rows * scale) 
    fig, axes = plot.plt.subplots(num_rows, num_cols, figsize = figs) 
    axes: np.ndarray = axes.flatten() #将axes转换为一维数组
    for index, (ax, image) in enumerate(zip(axes, images)):
        ax.imshow(image.numpy())
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False) 
        if titles is not None:
            ax.set_title(titles[index]) 
    return axes

def get_dataloader_workers():
    workers_count: int = 0
    if torch.cuda.is_available(): 
        workers_count = 4
    else:
        try:
            import multiprocessing 
            workers_count = multiprocessing.cpu_count()
        except ImportError:
            workers_count = 1
    return workers_count
