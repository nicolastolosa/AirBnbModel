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

from AirBnbModel.config import cfg
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

    users = source.read_csv(filename="train_users_2.csv")
    sessions = source.read_csv(filename="sessions.csv")

    # sessions.get_unique_IDs()

    # users.get_unique_IDs()

    # merge_datasets()

    # train_test_split()

    # store_data
    users_destination = os.path.join(DESTINATION_PATH, "users.csv")
    users.to_csv(users_destination, index=False)

    sessions_destination = os.path.join(DESTINATION_PATH, "sessions.csv")
    sessions.to_csv(sessions_destination, index=False)


def predict():
    """
    Defines the execution of the 'source' task on predict mode.

    This task extracts different tables containing new data loads it into
    a staging database, prior to its preprocessing.
    """

    df: pd.DataFrame
    destination: str

    # parameters to pass pd.to read_csv().
    source_params: dict = cfg.source.data.predict
    for dataset in source_params:

        df = pd.read_csv(**source_params[dataset])

        logger.info(
            f"""{df.shape[0]} rows and {df.shape[1]} colums loaded for
             {dataset} from {source_params[dataset]['filepath_or_buffer']}"""
        )
        logger.debug(f"{dataset} dataset structure preview:\n{df.head(2)}")

        destination = cfg.source.params.destination.predict[dataset]
        df.to_pickle(destination)

        logger.info(f"{dataset} dataset saved on {destination}")
