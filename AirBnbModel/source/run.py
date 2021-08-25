"""
Contains the functions that define the execution of the 'source' task, which
is responsible of extracting data from source database and loading it into
a staging database, so it can be preprocessed.

Functions on this script must be called from run.py on main package folder.

Configuration parameters for this task can be found on configs/config.yml
"""
import logging
import os
import shutil
import zipfile

import kaggle
import pandas as pd

from AirBnbModel.config import cfg

logger = logging.getLogger(__name__)


def train_eval():
    """
    Defines the execution of the 'source' task on train_eval mode.

    This task extracts different tables containing training data and the target
    variable and loads it into a staging database, prior to its preprocessing.
    """
    # Create connection and authenticate to kaggle API
    kaggle_api = kaggle.KaggleApi()
    kaggle_api.authenticate()

    COMPETITION_NAME = "airbnb-recruiting-new-user-bookings"
    TEMP_DESTINATION_PATH = "data/train/source/temp"
    try:
        # download_data
        os.makedirs(TEMP_DESTINATION_PATH, exist_ok=True)
        kaggle_api.competition_download_files(
            competition=COMPETITION_NAME, path=TEMP_DESTINATION_PATH
        )
        logger.info(f"Data downloaded in {TEMP_DESTINATION_PATH}")

        # unzip_data
        ZIP_PATH = os.path.join(TEMP_DESTINATION_PATH, COMPETITION_NAME + ".zip")
        training_datasets = ["train_users_2.csv.zip", "sessions.csv.zip"]
        with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
            zip_ref.extractall(TEMP_DESTINATION_PATH, training_datasets)
        os.remove(ZIP_PATH)  # Remove .zip after extracting its contents
        logger.info("main zip file extracted")

        for dataset in training_datasets:
            zip_path = os.path.join(TEMP_DESTINATION_PATH, str(dataset))

            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(TEMP_DESTINATION_PATH)

            os.remove(zip_path)
            logger.info(f"{dataset} extracted in {TEMP_DESTINATION_PATH}")

        # Read .csv files
        users_path = os.path.join(TEMP_DESTINATION_PATH, "train_users_2.csv")
        users = pd.read_csv(users_path)
        logger.info("users dataset loaded")

        sessions_path = os.path.join(TEMP_DESTINATION_PATH, "sessions.csv")
        sessions = pd.read_csv(sessions_path)
        logger.info("sessions dataset loaded")

    except Exception as e:
        logger.error(f"ERROR: {e}")

    finally:
        try:
            shutil.rmtree(TEMP_DESTINATION_PATH)
            logger.info(f"Temporary folder {TEMP_DESTINATION_PATH} deleted")
        except OSError as e:
            print("Error: %s : %s" % (TEMP_DESTINATION_PATH, e.strerror))

    # sessions.get_unique_IDs()

    # users.get_unique_IDs()

    # merge_datasets()

    # train_test_split()

    # store_data()
    DESTINATION_PATH = "data/train/source"

    users_destination_path = os.path.join(DESTINATION_PATH, "users.csv")
    users.to_csv(users_destination_path, index=False)
    logger.info(f"users dataset stored in {users_destination_path}")

    sessions_destination_path = os.path.join(DESTINATION_PATH, "sessions.csv")
    sessions.to_csv(sessions_destination_path, index=False)
    logger.info(f"sessions dataset stored in {sessions_destination_path}")

    # df: pd.DataFrame
    # destination: str

    # # parameters to pass pd.to read_csv().
    # source_params: dict = cfg.source.data.train_eval
    # for dataset in source_params:

    #     df = pd.read_csv(**source_params[dataset])

    #     logger.info(
    #         f"""{df.shape[0]} rows and {df.shape[1]} colums loaded for
    #         {dataset} from {source_params[dataset]['filepath_or_buffer']}"""
    #     )
    #     logger.debug(f"{dataset} dataset structure preview:\n{df.head(2)}")

    #     destination = cfg.source.params.destination.train_eval[dataset]
    #     df.to_pickle(destination)

    #     logger.info(f"{dataset} dataset saved on {destination}")


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
