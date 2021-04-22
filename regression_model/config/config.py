import pathlib
import regression_model

PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models'
DATASET_DIR = PACKAGE_ROOT / 'datasets'

TRAINING_DATA_FILE = 'insurance.csv'
TARGET = 'charges'

FEATURES = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

ENCODED_FEATURES = ['age', 'bmi', 'children', 'sex_female', 'sex_male', 'smoker_no',
       'smoker_yes', 'region_northeast', 'region_northwest',
       'region_southeast', 'region_southwest']

# Features can be dropped, so far none
DROP_FEATURES = []

# Numerical features with NA, no for this dataset
NUMERICAL_VARS_WITH_NA = []

# Categorical features with NA, no for this dataset
CATEGORICAL_VARS_WITH_NA = []

# No temporal variables
TEMPORAL_VARS = []

# Numerical variables to log transform
NUMERICAL_LOG_VARS = ['age', 'bmi']

# Categorical variables to encode
CATEGORICAL_VARS = ['sex', 'smoker', 'region']

# Numerical variables with outliers
NUMERICAL_VARS_WITH_OUTLIERS = ['bmi']

NUMERICAL_NA_NOT_ALLOWED = [feature for feature in FEATURES if feature not in CATEGORICAL_VARS + NUMERICAL_VARS_WITH_NA]
CATEGORICAL_NA_NOT_ALLOWED = [feature for feature in CATEGORICAL_VARS if feature not in CATEGORICAL_VARS_WITH_NA]

# Selected features for model fitting
SELECTED_FEATURES = ['age', 'bmi', 'children', 'sex_female', 'smoker_no', 
    'region_northeast', 'region_northwest', 'region_southeast', 'region_southwest']

# Model Params
FOREST_PARAMS = {
    'bootstrap': True,
    'max_depth': 5,
    'max_features': 'auto',
    'min_samples_leaf': 6,
    'min_samples_split': 2,
    'n_estimators': 300
    }