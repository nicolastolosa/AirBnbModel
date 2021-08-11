"""
Contains the functions that define the execution of the 'source' task, which
is responsible of extracting data from source database and loading it into
a staging database, so it can be preprocessed.

Functions on this script must be called from run.py on main package folder.

Configuration parameters for this task can be found on configs/config.yml
"""
import logging

import pandas as pd

from AirBnbModel.config import cfg

logger = logging.getLogger(__name__)


def train_eval():
    """
    Defines the execution of the 'source' task on train_eval mode.

    This task extracts different tables containing training data and the target
    variable and loads it into a staging database, prior to its preprocessing.
    """

    df: pd.DataFrame
    destination: str

    # parameters to pass pd.to read_csv().
    source_params: dict = cfg.source.data.train_eval
    for dataset in source_params:

        df = pd.read_csv(**source_params[dataset])

        logger.info(
            f"""{df.shape[0]} rows and {df.shape[1]} colums loaded for
            {dataset} from {source_params[dataset]['filepath_or_buffer']}"""
        )
        logger.debug(f"{dataset} dataset structure preview:\n{df.head(2)}")

        destination = cfg.source.params.destination.train_eval[dataset]
        df.to_pickle(destination)

        logger.info(f"{dataset} dataset saved on {destination}")


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
