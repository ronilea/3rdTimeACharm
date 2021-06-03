import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def preprocessing(df):
    print(df.shape)
    del df['IUCR']
    del df['Description']
    del df['FBI Code']
    del df['ID']
    del df['Case Number']
    del df['Year']
    del df['Updated On']
    df.dropna(inplace=True)
    del df['X Coordinate']
    del df['Y Coordinate']
    del df['Latitude']
    del df['Longitude']
    del df['Location']
    df = pd.get_dummies(df, columns=['Arrest'])
    print(df.shape)
    print('h')
    df.describe(include='all').to_csv("train_desc_after_filter.csv",index=False)


if __name__ == '__main__':
    train_data = pd.read_csv("train.csv")
    preprocessing(train_data)

