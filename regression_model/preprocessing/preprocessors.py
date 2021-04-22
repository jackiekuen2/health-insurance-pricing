import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from regression_model.config import config

class CategoricalEncoder(BaseEstimator, TransformerMixin):
    """Get dummy columns"""

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # to accomodate the pipeline
        return self

    def transform(self, X):
        X = X.copy()

        X_cate_encoded = pd.get_dummies(X[self.variables])
        X = X.drop(columns=self.variables, axis=1)
        X = pd.concat([X, X_cate_encoded], axis=1)
        
        # Re-label the columns to ensure consistent data size via pipeline
        X = X.reindex(labels=config.ENCODED_FEATURES, axis=1).fillna(0)

        return X

class LogTransformer(BaseEstimator, TransformerMixin):
    """Logarithm transformer"""

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, X, y=None):
        # to accomodate the pipeline
        return self
    
    def transform(self, X):
        X = X.copy()

        # check the values are non-negative for log-transform
        if not (X[self.variables] >0).all().all():
            vars_ = self.variables[(X[self.variables] <= 0).any()]
            raise ValueError(
                f"Variables contain zero or negative values, "
                f"can't apply log for vars: {vars_}"
            )
        
        for feature in self.variables:
            X[feature] = np.log(X[feature])

        return X


# # For testing
# if __name__ == '__main__':
#     df = pd.read_csv('regression_model/datasets/insurance.csv')

#     cate_encoding = CategoricalEncoder(['sex', 'smoker', 'region'])
#     data = cate_encoding.transform(df[0:10].drop(['charges'], axis=1))
#     print(df.head())
#     print(data.head(), data.shape)

#     log_trans = LogTransformer(['age', 'bmi'])
#     data = log_trans.transform(data)
#     print(data.head(), data.shape)