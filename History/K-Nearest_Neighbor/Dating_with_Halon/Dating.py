import pandas as pd
import matplotlib.pyplot as plt
import K_Nearest_Neighbor


def encoding(data: pd.DataFrame):
    encoding = {
        "didntLike": 0,
        "smallDoses": 1,
        "largeDoses": 2
    }
    for i in range(0, data.shape[0]):
        data.iloc[i, -1] = encoding[data.iloc[i, -1]]
    return data


def normalization(data: pd.DataFrame):
    for i in range(0, data.shape[1]-1):  # column
        max = data.iloc[:, i].max()
        min = data.iloc[:, i].min()
        for j in range(0, data.shape[0]):  # row
            data.iloc[j, i] = (data.iloc[j, i] - min) / (max - min)
    return data


def readfile(filename = "K-Nearest_Neighbor\Dating_with_Halon\datingTestSet.txt"):
    data = pd.read_csv(filename)
    data = normalization(encoding(data))
    return data


def visualization(data):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    t1: pd.DataFrame = data[data["likeability"] == 0]
    t2: pd.DataFrame = data[data["likeability"] == 1]
    t3: pd.DataFrame = data[data["likeability"] == 2]
    ax.scatter(t1.iloc[:, 0], t1.iloc[:, 1], t1.iloc[:, 2],
               marker="o", label="didntLike")
    ax.scatter(t2.iloc[:, 0], t2.iloc[:, 1], t2.iloc[:, 2],
               marker="^", label="smallDoses")
    ax.scatter(t3.iloc[:, 0], t3.iloc[:, 1], t3.iloc[:, 2],
               marker="s", label="largeDoses")

    ax.legend()  # Make legend, set axes limits and labels
    ax.set_zlabel('ice_cream_liter')
    ax.set_ylabel('gaming_percentage')
    ax.set_xlabel('frequent_flier_miles')
    plt.show()


def split_data(ratio: float, data: pd.DataFrame):
    line = int(data.shape[0]*ratio)
    data = data.sample(frac=1).reset_index(drop=True)
    return [data.iloc[0:line,:],data.iloc[line:,:]]

data = readfile()
test,train = split_data(0.2,data)

#visualization(test)
#visualization(train)

K_Nearest_Neighbor.classification(test,train,4)



