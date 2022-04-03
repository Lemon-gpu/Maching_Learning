from typing import Tuple
import torch
import numpy as np
import tools.plot as plot
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
