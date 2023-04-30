import numpy as np

from sklearn.preprocessing import normalize

def get_data():
    data = open("data.txt", "r")
    data = data.readlines()
    X = []
    y = []
    for data_item in data:
        data_item = data_item.split("\n")
        data_item = data_item[0]
        data_item = data_item.split(",")
        data_x = []
        data_item_y = data_item[-1]
        data_item.pop()
        for item in data_item:
            item = int(item)
            data_x.append(item)
        X.append(data_x)
        y.append(data_item_y)
    return X, y
