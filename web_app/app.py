from flask import Flask, render_template, flash, request, jsonify, Markup
import logging, io, os, sys
import pandas as pd
import json

from regression_model.preprocessing.data_management import load_pipeline
from regression_model.config import config
from regression_model.train_pipeline import run_training
from regression_model.predict import make_prediction

# # Model
# pipeline_file_name = 'regression_model.pkl'
# _insurance_pipeline = None


# Make an instance of Flask
app = Flask(__name__)

# Configure SECRET_KEY, which is needed to keep the client-side sessions secure in Flask
app.config['SECRET_KEY'] = 'someRandomKey'

# Check whether or not the model is trained, if no, train the model
if not os.path.isfile('regression_model/trained_models/regression_model.pkl'):
    run_training()

# @app.before_first_request
# def startup():
#     global _insurance_pipeline
#     _insurance_pipeline = load_pipeline(file_name=pipeline_file_name)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/background_process', methods=['POST', 'GET'])
def background_process():
    Age = request.args.get('age')
    Sex = request.args.get('sex')
    BMI = request.args.get('bmi')
    Children = request.args.get('children')
    Smoker = request.args.get('smoker')
    Region = request.args.get('region')

    # User inputs stored in JSON to be passed
    user_input = {}

    user_input['age'] = Age
    user_input['sex'] = Sex
    user_input['bmi'] = BMI
    user_input['children'] = Children
    user_input['smoker'] = Smoker
    user_input['region'] = Region

    user_input = json.dumps([user_input])
    result = make_prediction(input_data=user_input)

    # Convert numpy ndarray to list, and format
    predictions = "{:.2f}".format(result.get('predictions').tolist()[0])

    # Return the reponse as JSON
    return jsonify({'price_prediction': predictions})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)