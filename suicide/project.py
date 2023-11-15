import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from Health.data_ingestion import data_ingestion

class visualization:

    def __init__(self,path):

        self.df=data_ingestion(path).age_suicide()
    
        
    def plotPerColumnDistribution(self,nGraphShown, nGraphPerRow):
        print(self.df.head())
        nunique = self.df.nunique()
        
        
        df = self.df[[col for col in self.df if nunique[col] > 1 and nunique[col] < 50]]
        nRow, nCol = df.shape
        columnNames = list(df)
        nGraphRow = math.ceil((nCol + nGraphPerRow - 1) / nGraphPerRow)  
        plt.figure(num=None, figsize=(6 * nGraphPerRow, 8 * nGraphRow), dpi=80, facecolor='w', edgecolor='k')
        
        for i in range(min(nCol, nGraphShown)):
            
            plt.subplot(nGraphRow, nGraphPerRow, i + 1)
            columnDf = df.iloc[:, i]
            
        
            if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
                valueCounts = columnDf.value_counts()
                valueCounts.plot.bar()
            else:
                columnDf.hist()
            plt.ylabel('counts')
            plt.xticks(rotation=90)
            plt.title(f'{columnNames[i]} (column {i})')
        plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=1.0)
        plt.show()



    def plotCorrelationMatrix(self, graphWidth):
        filename = self.df
        df = self.df.select_dtypes(include='number')  # Select only numeric columns
        df = df.dropna()  # Drop rows with NaN in numeric columns

        if df.shape[1] < 2:
            print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
            return
            
        corr = df.corr()
        plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
        corrMat = plt.matshow(corr, fignum=1)
        plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
        plt.yticks(range(len(corr.columns)), corr.columns)
        plt.gca().xaxis.tick_bottom()
        plt.colorbar(corrMat)
        plt.title(f'Correlation Matrix for {filename}', fontsize=15)
        plt.show()



    # Scatter and density plots
    def plotScatterMatrix(self,plotSize, textSize):
        df = self.df.select_dtypes(include =[np.number]) # keep only numerical columns
        # Remove rows and columns that would lead to df being singular
        df = df.dropna()
        df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
        columnNames = list(df)
        if len(columnNames) > 10: # reduce the number of columns for matrix inversion of kernel density plots
            columnNames = columnNames[:10]
        df = df[columnNames]
        ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
        corrs = df.corr().values
        for i, j in zip(*plt.np.triu_indices_from(ax, k = 1)):
            ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
        plt.suptitle('Scatter and Density Plot')
        plt.show()

if __name__=='__main__':

    a=r'artifact\Age-standardized suicide rates.csv'
    b=r'artifact\Crude suicide rates.csv'
    c=r'artifact\Facilities.csv'
    print(f"Press 1 to see the visualization of Age-standardized, 2 to see the visualization of crude suicide rates and 3 to \
          see the visualization of Facilities ")
    v1=int(input())
    if v1==1:
        visualization(a)
        visualization(a).plotPerColumnDistribution(10, 5)
        visualization(a).plotCorrelationMatrix(8)
        visualization(a).plotScatterMatrix(1,1)
    if v1==2:
        visualization(b)
        visualization(b).plotPerColumnDistribution(10, 5)
        visualization(b).plotCorrelationMatrix(8)
        visualization(b).plotScatterMatrix(1,1)
    if v1==3:
        visualization(c)  
        visualization(c).plotPerColumnDistribution(10, 5)
        visualization(c).plotCorrelationMatrix(8)
        visualization(c).plotScatterMatrix(1,1)


