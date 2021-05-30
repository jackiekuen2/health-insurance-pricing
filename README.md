# Health Insurance Pricing Web App
Live Demo: https://health-insurance-pricing.herokuapp.com/
<img width="1424" alt="Screen Shot 2021-05-27 at 8 11 51 PM" src="https://user-images.githubusercontent.com/32947572/119823949-f5004f00-bf27-11eb-969f-498ce421bd3c.png">

## About The Project
This project aimed to provide an interactive webpage for user to input personal details and instantly get the annual price for health insurance plan. The algorithm used in ths project was Random Forest Regression. This project was an end-to-end project, with research stage using Jupyter Notebook and development stage applying Object-oriented programming (OOP), and the Flask web app was deployed to Heroku.

## Prerequisites
Main packages were used in this project:
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

Available: https://www.kaggle.com/mirichoi0218/insurance

Target variable: charges (Individual medical costs billed by health insurance)
Features: age, sex, BMI, children, smoker, regioN (the beneficiary's residential area in the US, northeast, southeast, southwest, northwest)

## Project Workflow
1. Research Stage in Jupyter Notebook: EDA, Data Visualizations, Base Models Evaluation, Hyperparameter Tuning with Grid-search CV (Kaggle Notebook: https://www.kaggle.com/jackiekuen/health-insurance-pricing)
2. Virtual environment setup, and required packages installation
3. Production scripting: config.py, preprocessors.py, pipeline.py, train_pipeline.py, predict.py
4. Testing with PyTest
5. Interactive web app design with Flask and HTML/CSS/JS
6. Deploying to Heroku

## Data Preprocessing
1. Outliers removal using IQR method
2. Encoding categorical variables
3. Log-transforming numerical variables
4. Feature scaling

## Models Evaluation
I first tried to train the model with different base algorithms, for examples: Linear Regression, Ridger Regression, Elastic Net, Decision Tree, XG-Boosting Regression, and Polynomial Linear Regression with different degrees.

Among all base models, Random Forest Regression, Gradient Boosting Regression, 2nd degree Polynomial Regression, and 3rd degree Polynomial Regression seemed to be promising, with lower RMSE.
<img width="883" alt="Screen Shot 2021-04-01 at 11 47 51 AM" src="https://user-images.githubusercontent.com/32947572/120105686-9d165200-c18c-11eb-98a1-e2e577d7f792.png">

## Hyperparameter Tuning
Next, after running Grid-Search CV, Random Forest Regression was the optimal solution among the above promising models.
<img width="869" alt="Screen Shot 2021-04-03 at 9 30 16 PM" src="https://user-images.githubusercontent.com/32947572/120106297-0e570480-c18f-11eb-94d8-55bd1dcf1d77.png">

<img width="923" alt="Screen20Shot202021-04-0420at2012 19 0620PM" src="https://user-images.githubusercontent.com/32947572/120106403-61c95280-c18f-11eb-8804-9f54b0d55341.png">
The Grid-Search CV result was then saved to config.py for easy access

## Training Resutls
The regression results looked pretty good, except some outliers

<img width="420" alt="Screen Shot 2021-04-07 at 2 00 20 AM" src="https://user-images.githubusercontent.com/32947572/120107135-66433a80-c192-11eb-91cc-cb7b28147376.png">

## Web App
The web app was created with Flask, and deployed to Heroku

Web App: https://health-insurance-pricing.herokuapp.com/

## References
- Designing an interactive web application to deploy the ML model using flask https://medium.com/@skumarr53/designing-an-interactive-web-application-to-deploy-the-ml-model-using-flask-9fef575600d2
- ML Data Pipelines with Custom Transformers in Python https://towardsdatascience.com/custom-transformers-and-ml-data-pipelines-with-python-20ea2a7adb65
- Creating Custom Transformers with Scikit-Learn https://towardsdatascience.com/creating-custom-transformers-using-scikit-learn-5f9db7d7fdb5
