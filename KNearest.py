from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def split_to_X_y(df):
    y_train = df.pop("Primary Type")
    X_train = df

class Neighbors:
    def __init__(self,X_train,y_train):
        self.nbrs = KNeighborsClassifier(n_neighbors=2, weights='distance', algorithm='ball_tree')
        self.nbrs.fit(X_train, y_train)

    def predict(self,X):
        return self.nbrs.predict(X)
