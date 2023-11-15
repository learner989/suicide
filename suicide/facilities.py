import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from suicide.data_ingestion import data_ingestion

class FacilitiesProcessor:
    def __init__(self,path):

        self.facilities=data_ingestion(path).age_suicide()

    def head1(self):
        print(self.facilities.head())
        return self.facilities.head()
    
    def drop_columns(self, columns):
        self.facilities = self.facilities.drop(columns=columns,axis=1)

    def fill_na_with_median(self, columns):
        for column in columns:
            self.facilities[column].fillna(self.facilities[column].median(), inplace=True)

    def remove_outliers(self, column, threshold):
        median = self.facilities[column].median()
        self.facilities[column] = np.where(self.facilities[column] > threshold, median, self.facilities[column])

    def plot_boxplot(self, column):
        sns.boxplot(x=self.facilities[column])
        plt.show()

    def plot_scatter(self, x_column, y_column):
        plt.scatter(self.facilities[x_column], self.facilities[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.show()

    def visualize_correlation(self):
        plt.figure(figsize=(7, 5))
        correlations = self.facilities.corr()
        sns.heatmap(correlations, cmap="BrBG", annot=True)
        plt.show()

    def visualize_histogram(self, column, bins=20):
        self.facilities[column].hist(bins=bins, alpha=0.9)
        plt.show()


if __name__=='__main__':

    facilities_df=r'artifact\Facilities.csv'
    facilities_processor = FacilitiesProcessor(facilities_df)
    print(facilities_processor.head1())

   