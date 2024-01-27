#1
import pandas as pd
import numpy as np

class data_description:

    def __init__(self, data):
        self.df = data

    def show_properties(self):

        numerics = self.df.select_dtypes(include=np.number)
        # calculate the properties of each column
        properties = numerics.agg(['mean', 'std', 'min', 'max', 'count'])
        # calculate the percentiles of each column
        percentiles = numerics.quantile([0.25, 0.5, 0.75])
        # append the percentiles to the properties
        properties = properties.append(percentiles)
        # rename the index of the properties
        properties.index = ['mean', 'std', 'min', 'max', 'count', '25%', '50%', '75%']
        # get the datatypes and null values of each column
        datatypes = numerics.dtypes
        nulls = numerics.isnull().sum()
        # create a new dataframe with the properties, datatypes and nulls
        summary = pd.DataFrame(properties)
        summary.loc['dtype'] = datatypes
        summary.loc['nulls'] = nulls
        # return the summary dataframe
        print(summary)

    def column_summary(self, col):
        # check if the column is numeric
        if np.issubdtype(self.df[col].dtype, np.number):
            # calculate the properties of the numeric column
            properties = self.df[col].agg(['mean', 'std', 'min', 'max', 'count'])
            # calculate the percentiles of the numeric column
            percentiles = self.df[col].quantile([0.25, 0.5, 0.75])
            # append the percentiles to the properties
            properties = properties.append(percentiles)
            # rename the index of the properties
            properties.index = ['mean', 'std', 'min', 'max', 'count', '25%', '50%', '75%']
            # return the properties as a series
            return properties
        # check if the column is string
        elif self.df[col].dtype == object:
            # calculate the properties of the string column
            properties = self.df[col].agg(['count', 'nunique'])
            # rename the index of the properties
            properties.index = ['total values', 'distinct values']
            # return the properties as a series
            return properties
        # otherwise, raise an exception
        else:
            raise ValueError("The column must be either numeric or string")

    # define a function that takes a dataframe and a number of rows as input and prints the dataset
    def print_dataset(self, n):
        # check if the number of rows is valid
        if n > 0 and n <= len(self.df):
            # print the first n rows of the dataframe
            print(self.df.head(n).to_string(index=False))
        else:
            # raise an exception
            raise ValueError("The number of rows must be positive and less than or equal to the length of the dataframe")

