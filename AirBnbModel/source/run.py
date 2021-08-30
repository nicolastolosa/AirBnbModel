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

# from AirBnbModel.config import cfg
from AirBnbModel.utils import kaggle

logger = logging.getLogger(__name__)


def train_eval():
    """
    Defines the execution of the 'source' task on train_eval mode.

    This task extracts different tables containing training data and the target
    variable and loads it into a staging database, prior to its preprocessing.
    """

    # Variable declaration
    COMPETITION_NAME: str = "airbnb-recruiting-new-user-bookings"
    DESTINATION_PATH: str = "data/train/source"

    users: pd.DataFrame
    sessions: pd.DataFrame

    # Extract data from source
    source = kaggle.CompetitionAPI(competition_name=COMPETITION_NAME)

    logger.info("Getting datasets from Kaggle competition API")
    users = source.read_csv(filename="train_users_2.csv", index_col="id")  # PARAMETRO
    sessions = source.read_csv(
        filename="sessions.csv", index_col="user_id"
    )  # PARAMETRO

    # Get unique user_id from both datasets before train_test_split().
    logger.info("Preparing data to train_test_split")
    cols = ["country_destination"]  # PARAMETRO
    users_unique_notnull_ids = (
        users[cols]
        .query("index.unique()", engine="python")
        .query("index.notnull()", engine="python")
        .rename_axis(index="user_id")  # PARAMETRO
    )

    sessions_unique_notnull_ids = pd.Series(
        sessions.index.unique().dropna().rename("user_id")  # PARAMETRO
    )

    valid_ids = pd.merge(
        left=users_unique_notnull_ids,
        right=sessions_unique_notnull_ids,
        how="inner",
        on="user_id",
    )

    # train_test_split
    TEST_SIZE = 0.2  # PARAMETRO
    logger.info(f"Splitting data into train and test datasets. Test size: {TEST_SIZE}")
    id_train, id_test = train_test_split(
        valid_ids.user_id,
        test_size=TEST_SIZE,
        stratify=valid_ids.country_destination,
        random_state=42,
    )

    users_train = users[users.index.isin(id_train)]
    users_test = users[users.index.isin(id_test)]

    sessions_train = sessions[sessions.index.isin(id_train)]
    sessions_test = sessions[sessions.index.isin(id_train)]

    # store_data
    os.makedirs(DESTINATION_PATH, exist_ok=True)
    users_destination = os.path.join(DESTINATION_PATH, "users.csv")
    users_train.to_csv(users_destination, index=False)

    sessions_destination = os.path.join(DESTINATION_PATH, "sessions.csv")
    sessions_train.to_csv(sessions_destination, index=False)

    logger.info(f"Training data saved into: {DESTINATION_PATH}")

    TEST_PATH = os.path.join(DESTINATION_PATH, "test")
    os.makedirs(TEST_PATH, exist_ok=True)

    users_destination = os.path.join(TEST_PATH, "users.csv")
    users_test.to_csv(users_destination, index=False)

    sessions_destination = os.path.join(TEST_PATH, "sessions.csv")
    sessions_test.to_csv(sessions_destination, index=False)

    logger.info(f"Test data saved into: {DESTINATION_PATH}")


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
    source = kaggle.CompetitionAPI(competition_name=COMPETITION_NAME)

    logger.info("Getting datasets from Kaggle competition API")
    users = source.read_csv(filename="test_users.csv", index_col="id")  # PARAMETRO
    sessions = source.read_csv(
        filename="sessions.csv", index_col="user_id"
    )  # PARAMETRO

    # Get unique user_id from both datasets.
    users_unique_notnull_ids = pd.Series(
        users.index.unique().dropna().rename("user_id")
    )

    sessions_unique_notnull_ids = pd.Series(
        sessions.index.unique().dropna().rename("user_id")  # PARAMETRO
    )

    valid_ids = pd.merge(
        left=users_unique_notnull_ids,
        right=sessions_unique_notnull_ids,
        how="inner",
        on="user_id",
    ).user_id

    users = users[users.index.isin(valid_ids)]
    sessions = sessions[sessions.index.isin(valid_ids)]

    # store_data
    os.makedirs(DESTINATION_PATH, exist_ok=True)
    users_destination = os.path.join(DESTINATION_PATH, "users.csv")
    users.to_csv(users_destination, index=False)

    sessions_destination = os.path.join(DESTINATION_PATH, "sessions.csv")
    sessions.to_csv(sessions_destination, index=False)

    logger.info(f"Data saved into: {DESTINATION_PATH}")
