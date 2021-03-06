"""
Contains the functions that define the training and evaluation scope of the
classification model of AirBnbModel Package.

Functions on this script must be called from run.py on main package folder.

Configuration parameters for this task can be found on configs/config.yml
"""
import logging
import os
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate

from AirBnbModel.config import cfg  # Configuration file

logger = logging.getLogger(__name__)


def main():
    """
    Defines the execution of the 'model' task on train_eval mode.

    This task extracts processed training and target data and uses it to train
    a classification model using Cross Validation.

    Finally, once the CV results have been saved, a new model is fitted and
    saved, using the full training dataset.
    """
    X: pd.DataFrame
    X_path: str

    Y: pd.Series
    Y_path: str

    cv_results: dict
    cv_results_df: pd.DataFrame
    destination_path: str

    # Loading data
    X_path = cfg.model.train_eval.data.X_path
    Y_path = cfg.model.train_eval.data.Y_path

    logger.info(f"Loading training data data from {X_path}")
    X = pd.read_pickle(X_path)

    logger.info(f"Loading training target data data from {Y_path}")
    Y = pd.read_pickle(Y_path).values.ravel()

    # Training and evaluating model
    cv_folds = cfg.model.train_eval.params.cv_folds
    eval_score = cfg.model.train_eval.params.eval_score

    model: RandomForestClassifier = RandomForestClassifier()

    cv_results = cross_validate(model, X, Y, cv=cv_folds, scoring=eval_score)
    logger.info(f"Model succesfully trained over CV {cv_folds} folds.")

    # Train model on the full dataset
    model.fit(X, Y)
    logger.info("Model retrained over full training dataset.")

    # Save model and results
    destination_path = cfg.model.train_eval.save_dir
    os.makedirs(destination_path, exist_ok=True)

    pickle.dump(model, open(destination_path + "/model" + ".pkl", "wb"))

    cv_results_df = pd.DataFrame(cv_results)
    cv_results_df.index.name = "fold"
    cv_results_df.to_csv(destination_path + "/results" + ".csv", index=False)
    logger.info(f"Model and results saved on {destination_path}.")
