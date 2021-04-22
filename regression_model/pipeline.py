from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler

from regression_model.preprocessing import preprocessors as pp
from regression_model.config import config


insurance_pipe = Pipeline([
    ('categorical_encoder', pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
    ('log_transformer', pp.LogTransformer(variables=config.NUMERICAL_LOG_VARS)),
    ('scaler', MinMaxScaler()),
    ('Random Forest Regressor', RandomForestRegressor(n_jobs=-1, random_state=0, **config.FOREST_PARAMS))
])