import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class OutlierRemover(BaseEstimator, TransformerMixin):
    """Remove outliers"""

    def __init__(self, variables=None, factor=1.5):
        self.factor = factor
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, data):
        # to accomodate the pipeline
        return

    def transform(self, data):
        data = data.copy()

        for feature in self.variables:
            q25 = np.percentile(data[feature], 25)
            q75 = np.percentile(data[feature], 75)
            iqr = q75 - q25
            lower_bound = q25 - (self.factor * iqr)
            upper_bound = q75 + (self.factor * iqr)
            data = data.drop(data[(data[feature] < lower_bound) | (data[feature] > upper_bound)].index)
        return data

# # For testing
# if __name__ == '__main__':
#     df = pd.read_csv('regression_model/datasets/insurance.csv')

#     print(df.shape)
#     print(df['bmi'].mean())
#     outlier_remover = OutlierRemover(['bmi'])
#     data = outlier_remover.transform(df)
#     print(data['bmi'].mean())
#     print(data.shape)
#     print(data.head())