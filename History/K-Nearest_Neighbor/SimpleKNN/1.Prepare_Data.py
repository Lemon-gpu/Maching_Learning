import numpy as np
import pandas as pd


def create_dataset():
    data = {
        "romance": [(1, 101), (5, 89)],
        "action": [(108, 5), (115, 8)]
    }
    return pd.DataFrame(data)


print(create_dataset())
