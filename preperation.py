import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

CRIME_PRIMARY = {'BATTERY':0, 'THEFT':1, 'CRIMINAL DAMAGE':2, 'DECEPTIVE '
                                                              'PRACTICE':3,
                 'ASSAULT':4}
def preprocessing(df):
    print(df.shape)
    del df['IUCR']
    del df['Description']
    del df['FBI Code']
    del df['ID']
    del df['Case Number']
    del df['Year']
    del df['Updated On']
    del df['Unnamed: 0']
    df.dropna(inplace=True)
    del df['X Coordinate']
    del df['Y Coordinate']
    del df['Latitude']
    del df['Longitude']
    del df['Location']
    df = pd.get_dummies(df, columns=['Arrest'])
    df = pd.get_dummies(df, columns=['Domestic'])
    df = pd.get_dummies(df, columns=['District'])
    df['Date'] = pd.to_datetime(df.Date)
    df.replace(to_replace=CRIME_PRIMARY, inplace=True)
    print(df.dtypes)
    # df.describe(include='all').to_csv("train_desc_after.csv",index=False)


if __name__ == '__main__':
    train_data = pd.read_csv("train.csv")
    preprocessing(train_data)

