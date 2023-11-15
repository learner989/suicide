print('dsvf ')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class data_ingestion:

    def __init__(self,a):
        self.a=a
    def age_suicide(self):
        df=pd.read_csv(self.a)
        print('1st 5 rows are \n')

        print(df.head())

        print('Null value in the dataset \n')

        print(df.isnull().sum())

        
        print('shape of the dataset is \n')
    

        print(f'There are {df.shape[0]} rows and {df.shape[1]} columns')
        return df


    def crude_suicide_rates(self):

        df=pd.read_csv(self.b)
        print(df.head())
        print(f'There are {df.shape[0]} rows and {df.shape[1]} columns')
        return df

    def facilities(self):
        df=pd.read_csv(self.c)
        print(df.head())
        print(f'There are {df.shape[0]} rows and {df.shape[1]} columns')
        return df

a=r'artifact\Age-standardized suicide rates.csv'

if __name__=='__main__':
    print(data_ingestion(a).age_suicide())
    
