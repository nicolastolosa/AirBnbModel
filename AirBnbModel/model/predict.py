import logging
import pickle
import os

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate

from AirBnbModel.config import cfg # Configuration file


logger = logging.getLogger(__name__)


def main():
    X: pd.DataFrame
    X_path: str

    model_path: str

    predictions: pd.Series
    destination_path: str



    # Loading data
    X_path = cfg.model.predict.data.X_path

    logger.info(f"Loading training data data from {X_path}")
    X = pd.read_pickle(X_path)

    # Loading model
    model_path = cfg.model.train_eval.save_dir + "/model.pkl"

    logger.info(f"Loading model from {model_path}")
    model = pickle.load(open(model_path, 'rb'))



    # Generating predictions
    predictions = pd.Series(model.predict(X), index = X.index)




    # Save predictions
    destination_path = cfg.model.predict.save_dir
    os.makedirs(destination_path, exist_ok=True) 

    predictions.to_csv(destination_path + "/predictions" + ".csv", index = True)




