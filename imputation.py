#2

import pandas as pd
import numpy as np

class imputataion:
    def __init__(self, data):
        self.df = data

    def print_null_count(df):
        # use the isnull() method to check for null values and sum() method to count them
        nulls = df.isnull().sum()
        # print the nulls as a series
        print(nulls.to_string())

# define a function that takes a dataframe and a column name as input and removes the column
    def remove_column(self, col):
        # check if the column name is valid
        if col in self.df.columns:
            # drop the column and return the modified dataframe
            self.df.drop(col, axis=1)
            return self.df
        else:
            # raise an exception
            raise ValueError("The column name does not exist in the dataframe")

    # define a function that fills the null values in a column with mean
    def fill_mean(self, col):
        # check if the column is numeric
        if np.issubdtype(self.df[col].dtype, np.number):
            # calculate the mean of the column
            mean = self.df[col].mean()
            # fill the null values with the mean
            self.df[col].fillna(value=mean, inplace=True)
            return self.df
        else:
            # raise an exception
            raise ValueError("The column must be numeric")

    # define a function that fills the null values in a column with median
    def fill_median(self, col):
        # check if the column is numeric
        if np.issubdtype(self.df[col].dtype, np.number):
            # calculate the median of the column
            median = self.df[col].median()
            # fill the null values with the median
            self.df[col].fillna(value=median, inplace=True)
            return self.df
        else:
            # raise an exception
            raise ValueError("The column must be numeric")

    # define a function that fills the null values in a column with mode
    def fill_mode(self, col):
        # calculate the mode of the column
        mode = self.df[col].mode()[0]
        # fill the null values with the mode
        self.df[col].fillna(value=mode, inplace=True)
        return self.df

    def display(self):
        print(self.df.head())
