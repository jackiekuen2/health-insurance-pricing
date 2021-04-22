import numpy as np
import pandas as pd

from regression_model.preprocessing.data_management import load_pipeline
from regression_model.config import config

pipeline_file_name = 'regression_model.pkl'
_insurance_pipeline = load_pipeline(file_name=pipeline_file_name)

def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline"""

    data = pd.read_json(input_data)
    prediction = _insurance_pipeline.predict(data[config.FEATURES])
    
    response = {"predictions": prediction}
    return response

# import json
# if __name__ == "__main__":
#     user_input = {
#         'age': 25,
#         'sex': 'male',
#         'bmi': 23,
#         'smoker': 'no',
#         'children': 2,
#         'region': 'southeast'
#     }
#     data = json.dumps([user_input])
#     # data = pd.read_json(data)
#     # print(data)
#     print(make_prediction(input_data=data))