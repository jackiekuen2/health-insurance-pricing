# Health Insurance Pricing Web App

## About The Project
This project aims to provide an interactive webpage for user to input personal details and instantly get the annual price for health insurance plan. The algorithm used in ths project is Random Forest Regressor.

## Prerequisites
The following main packages are used in this project:
- Numpy
- Pandas
- Scikit-Learn
- Pytest
- Flask
- Gunicorn

## Folder Structure
```
.
├── regression_model
│   ├── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   └── config.py
│   ├── datasets
│   │   ├── __init__.py
│   │   └── insurance.csv
│   ├── pipeline.py
│   ├── predict.py
│   ├── preprocessing
│   │   ├── __init__.py
│   │   ├── data_management.py
│   │   ├── outlier_remover.py
│   │   └── preprocessors.py
│   ├── train_pipeline.py
│   └── trained_models
│       └── regression_model.pkl
├── requirements.txt
├── tests
│   ├── __init__.py
│   └── test_predict.py
├── tox.ini
└── web_app
    ├── __init__.py
    ├── app.py
    ├── static
    │   └── health-insurance.jpg
    └── templates
        └── index.html
```


## Dataset
Medical Cost Personal Datasets from Kaggle includes health insurance prices for individuals in US
https://www.kaggle.com/mirichoi0218/insurance

Target variable:
- charges: Individual medical costs billed by health insurance

Features:
- age: age of primary beneficiary
- sex: insurance contractor gender, female, male
- bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height,
objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
- children: Number of children covered by health insurance / Number of dependents
- smoker: Smoking
- region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.

## Project Workflow
1. Research Stage with Jupyter Notebook: EDA, Data Visualizations, Base Models Training, Hyperparameters Tuning
2. Set up virtual environment, and install required packages
3. Production scripting: config.py, preprocessors.py, pipeline.py, train_pipeline.py, predict.py
4. Test with PyTest
5. Design UI with HTML/CSS/JS
6. Deploy to Heroku

## Data Preprocessing
1. Outliers removal using IQR method
2. 

## Web App
URL: https://health-insurance-pricing.herokuapp.com/
<img width="1424" alt="Screen Shot 2021-05-27 at 8 11 51 PM" src="https://user-images.githubusercontent.com/32947572/119823949-f5004f00-bf27-11eb-969f-498ce421bd3c.png">


## Research Stage
For documentation, visit the notebook https://www.kaggle.com/jackiekuen/health-insurance-pricing
