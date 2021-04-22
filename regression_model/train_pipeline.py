import numpy as np
from sklearn.model_selection import train_test_split

from regression_model import pipeline
from regression_model.config import config
from regression_model.preprocessing.outlier_remover import OutlierRemover
from regression_model.preprocessing.data_management import load_dataset, save_pipeline

def run_training() -> None:
    """Train the model"""

    # Read training data
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # Remove outliers
    outlier_remover = OutlierRemover(variables=config.NUMERICAL_VARS_WITH_OUTLIERS)
    data = outlier_remover.transform(data)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES], data[config.TARGET], 
        test_size=0.1, random_state=0
        )

    # Model fitting
    print("Training the model...")
    pipeline.insurance_pipe.fit(X_train[config.FEATURES], y_train)
    save_pipeline(pipeline_to_persist=pipeline.insurance_pipe)

if __name__ == '__main__':
    run_training()