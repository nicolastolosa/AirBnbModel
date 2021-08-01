import os
import logging

import pandas as pd

from AirBnbModel.config import cfg # Configuration file


logger = logging.getLogger(__name__)


def main(mode):
    '''
    Docstring

    '''


    source_config: dict
    df: pd.DataFrame
    destination: str


    # dict containing the parameters of the files to extract to pass pd.to read_csv().
    # Some metadata such as the path, depends on the execution mode (train/predict)
    source_config = cfg.source.data[mode]    
    for data in source_config:
        
        df = pd.read_csv(**source_config[data])
        
        logger.info(f"{df.shape[0]} rows and {df.shape[1]} colums loaded for {data} from {source_config[data]['filepath_or_buffer']}")
        logger.debug(f"{data} dataset structure preview:\n{df.head(2)}")


        destination = cfg.source.params.destination[mode][data]
        df.to_pickle(destination)

        logger.info(f"{data} dataset saved on {destination}")





# def read_csv_from_dict(config: dict) -> pd.DataFrame:
#     """Returns a pandas DataFrame object, passing the parameters given in 
#        config dict to pandas.read_csv() function.

#     Parameters
#     ----------
#     config
#         Python dict object containing the arguments that should be given to
#         pandas.read_csv().
    
#     Examples
#     --------
#     Extract a pandas DataFrame object located in 'filepath_or_buffer'.
#     Only 'usecols' columns are selected and 'index_col' column is used as index.

#     >>> read_csv_from_dict(config = {
#         'filepath_or_buffer'='folder/data.csv',
#         'usecols':['column1','column2'],
#         'index_col':['index_column']})

#     """


#     sig = inspect.signature(pd.read_csv)
#     param_list = [param.name for param in sig.parameters.values()]
#     print(param_list)
    


