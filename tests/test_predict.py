import math
from regression_model.predict import make_prediction
from regression_model.preprocessing.data_management import  load_dataset
from regression_model.config import config



def test_make_single_prediction():

    # Given
    test_data = load_dataset(file_name=config.TRAINING_DATA_FILE)
    test_data.drop(['charges'], axis=1, inplace=True)
    single_test_json = test_data[0:1].to_json(orient='records')
    # single_test_json = test_data.iloc[0:1, :-1].to_json(orient='records')

    # When
    subject = make_prediction(input_data=single_test_json)

    assert subject is not None
    assert isinstance(subject.get('predictions')[0], float)
    assert math.ceil(subject.get('predictions')[0]) == 17323

    # return subject

# if __name__ == '__main__':
    # print(test_make_single_prediction())
