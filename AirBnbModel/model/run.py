import logging

from AirBnbModel.model.train_eval import main as main_train_eval
from AirBnbModel.model.predict import main as main_predict


logger = logging.getLogger(__name__)


def main(mode):
    try:
        assert mode in ('train_eval', 'predict'), f"Selected mode ({mode}) is not valid. Mode should be one of 'train_eval', 'predict'"
    except:
        logger.error(f"Selected mode ({mode}) is not valid. Mode should be one of 'train_eval', 'predict'")
        raise

    if mode == 'train_eval':
        logger.info(f"Running training of the model")
        main_train_eval()
    else:
        logger.info(f"Running predictions")
        main_predict()