#3
import pandas as pd

class encoding:
    def __init__(self,data):
        self.df = data

    def unique_count(self, col):
        # use the nunique() method to count the unique values, excluding NaN values
        print(self.df[col].nunique(dropna=True))

    def one_hot_encoding(self, col):
        col = list(col)
        one_hot_encoded_data = pd.get_dummies(self.df, columns=col)
        self.df = one_hot_encoded_data
        return self.df

    def display(self):
        print(self.df.head())