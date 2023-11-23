import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class data_ingestion:

    def __init__(self,path):
        self.path=path
    def read(self):
        df=pd.read_csv(self.path)
        print('1st 5 rows are \n')

        print(df.head())

        print('Null value in the dataset \n')

        print(df.isnull().sum())

        
        print('shape of the dataset is \n')
    

        print(f'There are {df.shape[0]} rows and {df.shape[1]} columns')
        return df


path=r'artifact\Age-standardized suicide rates.csv'

if __name__=='__main__':
    print(data_ingestion(path).read())
    
