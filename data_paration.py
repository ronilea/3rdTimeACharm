import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def partion():
    dataset = pd.read_csv("Dataset_crimes.csv")
    train_set, test_set = train_test_split(dataset, test_size=0.30, random_state=1)
    val_test, test_set = train_test_split(test_set, test_size=0.5, random_state=1)
    train_set.to_csv("train.csv", index=False)
    test_set.to_csv("test.csv", index=False)
    val_test.to_csv("validate.csv", index=False)
    return


if __name__ == '__main__':

    print("hi")

