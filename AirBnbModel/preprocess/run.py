import os
import logging

import pandas as pd

from AirBnbModel.config import cfg # Configuration file


logger = logging.getLogger(__name__)


def main(mode):

    path: str
    users: pd.DataFrame
    preprocessed_users: pd.DataFrame
    destination: str

    
    # Load user data
    path = cfg.source.params.destination[mode]['users']
    users = pd.read_pickle(path)
    logger.info(f"User data loaded for preprocessing from {path}")


    # Assert key user data properties
    assert len(users.columns) == 2, f'2 columns expected on user dataset and got {len(users.columns)}.'
    assert users.index.duplicated().sum() == 0, f'Duplicated values on users index.'
    logger.info(f"User key data properties have been validated")


    # Transform user data
    preprocessed_users = users
    logger.info(f"User data has been preprocessed")

    
    # Save user data
    destination = cfg.preprocess.params.destination[mode]['X']
    preprocessed_users.to_pickle(destination)
    logger.info(f"User data preprocessing finished, data saved on {destination}")



    if(mode == 'train_eval'): # Load and assert target data only in train_eval mode

        # Load target data
        path = cfg.source.params.destination[mode]['target']
        target = pd.read_pickle(path)
        logger.info(f"target data loaded for validation from {path}")
        

        # Assert target data
        assert len(target.columns) == 1, f'1 columns expected on user dataset and got {len(target.columns)}.'
        assert target.index.duplicated().sum() == 0, f'Duplicated values on target index.'
        logger.info(f"Target key data properties have been validated")


        # Save key target data properties
        destination = cfg.preprocess.params.destination[mode]['target']
        target.to_pickle(destination)
        logger.info(f"Target data preprocessing finished, data saved on {destination}")
