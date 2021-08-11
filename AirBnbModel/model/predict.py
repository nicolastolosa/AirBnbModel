"""
Contains the functions that define the process for generating predictions for
the classification model of AirBnbModel Package.

Functions on this script must be called from run.py on main package folder.

Configuration parameters for this task can be found on configs/config.yml
"""
import logging
import os
import pickle

import pandas as pd

from AirBnbModel.config import cfg  # Configuration file

logger = logging.getLogger(__name__)


def main():
    """
    Defines the execution of the 'model' task on train_eval mode.

    This task extracts processed data and uses the model generated during the
    execution of 'model' task on 'train_eval' mode, to generate predictions.

    Once the predictions have been generated, they are saved on a new folder.
    """
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
    model = pickle.load(open(model_path, "rb"))

    # Generating predictions
    predictions = pd.Series(model.predict(X), index=X.index)

    # Save predictions
    destination_path = cfg.model.predict.save_dir
    os.makedirs(destination_path, exist_ok=True)

    predictions.to_csv(destination_path + "/predictions" + ".csv", index=True)
