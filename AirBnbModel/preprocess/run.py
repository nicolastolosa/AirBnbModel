"""
Contains the functions that define the execution of the 'preprocess' task,
which is responsible of loading data extracted by 'source' task, preprocessing
it and saved into a new folder, so it can be fed into a ML model.

Functions on this script must be called from run.py on main package folder.

Configuration parameters for this task can be found on configs/config.yml

"""
import logging

import pandas as pd

from AirBnbModel.config import cfg  # Configuration file

logger = logging.getLogger(__name__)


def train_eval():
    """
    Defines the execution of the 'preprocess' task on train_eval mode.

    This task loads training data from staging database, combines, generates
    new features and fits different preprocessing parameters, in order to
    input missing values.
    """

    path: str
    users: pd.DataFrame
    preprocessed_users: pd.DataFrame
    destination: str

    # Load user data
    path = cfg.source.params.destination.train_eval["users"]
    users = pd.read_pickle(path)
    logger.info(f"User data loaded for preprocessing from {path}")

    # Assert key user data properties
    assert (
        len(users.columns) == 2
    ), f"2 columns expected on user dataset and got {len(users.columns)}."
    assert users.index.duplicated().sum() == 0, "Duplicated values on users index."
    logger.info("User key data properties have been validated")

    # Transform user data
    preprocessed_users = users
    logger.info("User data has been preprocessed")

    # Save user data
    destination = cfg.preprocess.params.destination.train_eval["X"]
    preprocessed_users.to_pickle(destination)
    logger.info(f"User data preprocessing finished, data saved on {destination}")

    # Load target data
    path = cfg.source.params.destination.train_eval["target"]
    target = pd.read_pickle(path)
    logger.info(f"target data loaded for validation from {path}")

    # Assert target data
    assert (
        len(target.columns) == 1
    ), f"1 columns expected on user dataset and got {len(target.columns)}."
    assert target.index.duplicated().sum() == 0, "Duplicated values on target index."
    logger.info("Target key data properties have been validated")

    # Save key target data properties
    destination = cfg.preprocess.params.destination.train_eval["target"]
    target.to_pickle(destination)
    logger.info(f"Target data preprocessing finished, data saved on {destination}")


def predict():
    """
    Defines the execution of the 'preprocess' task on predict mode.

    This task loads new data from staging database, combines, generates new
    features and uses the parameters fitted on train_eval execution of the
    task, to input missing values over the data.
    """

    path: str
    users: pd.DataFrame
    preprocessed_users: pd.DataFrame
    destination: str

    # Load user data
    path = cfg.source.params.destination.predict["users"]
    users = pd.read_pickle(path)
    logger.info(f"User data loaded for preprocessing from {path}")

    # Assert key user data properties
    assert (
        len(users.columns) == 2
    ), f"2 columns expected on user dataset and got {len(users.columns)}."

    assert users.index.duplicated().sum() == 0, "Duplicated values on users index."
    logger.info("User key data properties have been validated")

    # Transform user data
    preprocessed_users = users
    logger.info("User data has been preprocessed")

    # Save user data
    destination = cfg.preprocess.params.destination.predict["X"]
    preprocessed_users.to_pickle(destination)
    logger.info(
        f"""User data preprocessing finished,
                data saved on {destination}"""
    )
