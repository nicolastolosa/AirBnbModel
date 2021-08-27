"""
Contains classes and methods needed to connect to Kaggle API and extract data
from it.

See also
----------

See https://www.kaggle.com/docs/api#authentication for details on the
authentication requierements to use the API.

"""

import logging
import os
import tempfile
import zipfile

import pandas as pd


# kaggle creates a connection and validates authentication on import. If
# import fails due to an authentication error, AuthenticationError is raised.
class AuthenticationError(Exception):
    """Exception to handle authentication failure on Kaggle API."""

    pass


try:
    import kaggle
    from kaggle.rest import ApiException
except OSError as e:
    if str(e).find("Could not find kaggle.json") != -1:
        raise AuthenticationError(
            f"{e} See https://www.kaggle.com/docs/api#authentication for details on the authentication requierements to use the API."
        ) from None
    else:
        raise

logger = logging.getLogger(__name__)


class CompetitionAPI:
    """
    Object that holds a connection to the Kaggle API with several methods to
    retreive data about competitions.

    Parameters
    ----------
    competition_name : str
        name of the Kaggle competition to which the connection will be
        stablished. competition_name can be extracted from the URL of the
        homepage of the competition kaggle.com/c/competition_name
    """

    def __init__(self, competition_name: str):
        self.api = kaggle.KaggleApi()
        self.api.authenticate()
        self.competition_name = competition_name

    def read_csv(self, filename: str, **kwargs) -> pd.DataFrame:
        """
        Reads comma-separated values (csv) dataset from Kaggle competition
        into a pandas DataFrame.

        Parameters
        ----------
        filename
            name of the .csv file to return. Se
            :func:`~CompetitionAPI.download_dataset` method's documentation
            for specifications on the format.

            **kwargs
                additional arguments passed to pandas.read_csv() method.

        Returns
        ----------
        pandas.DataFrame
            Returns the selected dataset of the competition as a DataFrame.

        Raises
        ----------
        AssertionError
            If filename has not a .csv extension.

        Examples
        --------
        returns sessions.csv dataset from Kaggle competition
        airbnb-recruiting-new-user-bookings, as a pandas DataFrame.

        >>> competition = CompetitionAPI('airbnb-recruiting-new-user-bookings')
        >>> competition.read_csv('sessions.csv')

        """

        assert (
            os.path.splitext(filename)[-1] == ".csv"
        ), f"{filename} is not a .csv file"
        zipped_filename = filename + ".zip"

        with tempfile.TemporaryDirectory() as tmpdir:
            # Download file using Kaggle API
            self.download_dataset(path=tmpdir, filename=zipped_filename)

            # Unpack .zip to extract .csv file
            zipped_filepath = os.path.join(tmpdir, zipped_filename)
            with zipfile.ZipFile(zipped_filepath, "r") as zip:
                zip.extractall(tmpdir)

            # read csv
            csv_filepath = os.path.join(tmpdir, filename)
            df = pd.read_csv(csv_filepath, **kwargs)

        return df

    def download_dataset(self, path: str, filename: str):
        """
        Downloads kaggle competition dataset specifyed in filename into path.

        Parameters
        ----------
        path
            relative or absolute path of the directory where downloaded
            dataset should be stored.
        filename
            name of the file to return. It must be one of the names
            returned by :func:`~CompetitionAPI.dataset_list` method.

        Raises
        ----------
        FileNotFoundError :
            If the dataset passed was not found in Kaggle API.

        Examples
        --------
        downloads sessions.csv.zip dataset from Kaggle competition
        airbnb-recruiting-new-user-bookings into documents/ directory.

        >>> competition = CompetitionAPI('airbnb-recruiting-new-user-bookings')
        >>> competition.read_csv('documents/', 'sessions.csv.zip')

        """
        try:
            self.api.competition_download_file(
                competition=self.competition_name,
                path=path,
                file_name=filename,
                quiet=True,
            )

        except ApiException as e:
            error_msg = (
                f"Unable to find {filename} in {self.competition_name} competition"
            )
            logger.exception(e)
            raise FileNotFoundError(error_msg)

        logger.info(
            f"{filename} succesfully downloaded from {self.competition_name} Kaggle competition"
        )

    def dataset_list(self) -> list[str]:
        """
        Lists all the datasets available to be accessed with Kaggle API for
        a certain competition.

        Returns
        ----------
        list of str
            Available datasets for the kaggle competition.

        """
        return self.api.competition_list_files(self.competition)
