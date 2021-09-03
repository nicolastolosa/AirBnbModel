"""
Contains the functions that define the execution of the 'source' task, which
is responsible of extracting data from source database and loading it into
a staging database, so it can be preprocessed.

Functions on this script must be called from run.py on main package folder.

Configuration parameters for this task can be found on configs/config.yml
"""
import logging
import os

import pandas as pd
from sklearn.model_selection import train_test_split

from AirBnbModel.source.processing import intersect_index
from AirBnbModel.utils import kaggle

logger = logging.getLogger(__name__)


def train_eval():
    """
    Defines the execution of the 'source' task on train_eval mode.

    This task extracts different tables containing training data and the target
    variable and loads it into a staging database, before to its preprocessing.
    """

    # Variable declaration
    COMPETITION_NAME: str = "airbnb-recruiting-new-user-bookings"
    TRAIN_PATH: str = "data/train/source"
    TEST_PATH: str = "data/test/source"

    users: pd.DataFrame
    sessions: pd.DataFrame

    # Extract data from source
    logger.info("Getting datasets from Kaggle competition API")

    source = kaggle.CompetitionAPI(competition_name=COMPETITION_NAME)

    users = source.read_csv(filename="train_users_2.csv", index_col="id")
    sessions = source.read_csv(filename="sessions.csv", index_col="user_id")

    # Get unique user_id from both datasets before train_test_split().
    logger.info("Preparing data to train_test_split")

    # valid_ids = join_on_unique_index(users, sessions)

    valid_ids = intersect_index(users, sessions)

    # train_test_split
    target = ["country_destination"]  # PARAMETRO
    TEST_SIZE = 0.2  # PARAMETRO

    logger.info(
        "Splitting data into train and test datasets." f"Test size: {TEST_SIZE}"
    )

    id_train, id_test = train_test_split(
        valid_ids,
        test_size=TEST_SIZE,
        stratify=users.loc[valid_ids, target],
        random_state=42,
    )

    users_train = users.loc[id_train, :]
    users_test = users.loc[id_test, :]

    sessions_train = sessions.loc[id_train, :]
    sessions_test = sessions.loc[id_test, :]

    # store training data
    os.makedirs(TRAIN_PATH, exist_ok=True)

    users_train.to_csv(TRAIN_PATH + "/users.csv", index=False)
    sessions_train.to_csv(TRAIN_PATH + "/sessions.csv", index=False)
    logger.info(f"Training data saved into: {TRAIN_PATH}")

    # store test data
    os.makedirs(TEST_PATH, exist_ok=True)

    users_test.to_csv(TEST_PATH + "/users.csv", index=False)
    sessions_test.to_csv(TEST_PATH + "/sessions.csv", index=False)
    logger.info(f"Test data saved into: {TEST_PATH}")


def predict():
    """
    Defines the execution of the 'source' task on predict mode.

    This task extracts different tables containing new data loads it into
    a staging database, prior to its preprocessing.
    """

    # Variable declaration
    COMPETITION_NAME: str = "airbnb-recruiting-new-user-bookings"
    DESTINATION_PATH: str = "data/predict/source"

    users: pd.DataFrame
    sessions: pd.DataFrame

    # Extract data from source
    logger.info("Getting datasets from Kaggle competition API")

    source = kaggle.CompetitionAPI(competition_name=COMPETITION_NAME)
    # FALTAN PARAMETROS
    users = source.read_csv(filename="test_users.csv", index_col="id")
    sessions = source.read_csv(filename="sessions.csv", index_col="user_id")

    # Valid users are those available in both users and sessions datasets.
    valid_ids = intersect_index(users, sessions)

    users_valid = users.loc[valid_ids, :]
    sessions_valid = sessions.loc[valid_ids, :]

    # store_data
    os.makedirs(DESTINATION_PATH, exist_ok=True)

    users_valid.to_csv(DESTINATION_PATH + "/users.csv", index=False)
    sessions_valid.to_csv(DESTINATION_PATH + "/sessions.csv", index=False)
    logger.info(f"Data saved into: {DESTINATION_PATH}")
