from typing import Tuple
import pandas as pd
import numpy as np
import struct


def read_label_in_idx1_ubyte(path: str) -> Tuple[int, int, pd.DataFrame]:
    file = open(path, mode="rb")
    magic_number, count = struct.unpack(">ii", file.read(8))
    labels = np.fromfile(file=file, dtype=np.uint8)
    labels = pd.DataFrame(labels)
    return magic_number, count, labels


def read_image_in_idx3_ubyte(path: str) -> Tuple[int, int, int, int, pd.DataFrame]:
    file = open(path, mode="rb")
    magic_number, count, rows, columns = struct.unpack(">iiii", file.read(16))
    images: np.array = np.fromfile(file=file, dtype=np.uint8)
    images = images.reshape(count, (rows*columns))
    images = pd.DataFrame(images)
    return magic_number, count, rows, columns, images


demo_train_labels = read_label_in_idx1_ubyte(
    "MNIST/train-labels-idx1-ubyte/train-labels.idx1-ubyte")[-1]
demo_train_images = read_image_in_idx3_ubyte(
    "MNIST/train-images-idx3-ubyte/train-images.idx3-ubyte")[-1]
demo_test_labels = read_label_in_idx1_ubyte(
    "MNIST/t10k-labels-idx1-ubyte/t10k-labels.idx1-ubyte")[-1]
demo_test_images = read_image_in_idx3_ubyte(
    "MNIST/t10k-images-idx3-ubyte/t10k-images.idx3-ubyte")[-1]
