import pandas as pd
import numpy as np


def load_dataset():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # 切分的词条
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak',
                       'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    postingList = pd.DataFrame(postingList)
    postingList.insert(postingList.shape[1], "label", classVec)
    return postingList

def create_vocabulary_table(data: pd.DataFrame):
    

temp = load_dataset()

