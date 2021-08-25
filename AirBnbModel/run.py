"""
Contains the main function of the package, which defines the execution of the
package. main() has been decorated with 'click' so it can process command
parameters.
"""

import logging

import click

from AirBnbModel.model.predict import main as model_predict
from AirBnbModel.model.train_eval import main as model_train_eval
from AirBnbModel.preprocess.run import predict as preprocess_predict
from AirBnbModel.preprocess.run import train_eval as preprocess_train_eval
from AirBnbModel.source.run import predict as source_predict
from AirBnbModel.source.run import train_eval as source_train_eval

logger = logging.getLogger(__name__)

tasks: dict = {
    "source": {"train_eval": source_train_eval, "predict": source_predict},
    "preprocess": {"train_eval": preprocess_train_eval, "predict": preprocess_predict},
    "model": {"train_eval": model_train_eval, "predict": model_predict},
}
mode: list = ["train_eval", "predict"]


def main(task: str, mode: str):
    """
    Acts as a single entry point to all the functionallity of the package.

    Parameters
    ----------
    task : {'source', 'preprocess', 'model'}
        the name of the task in the pipeline to be executed
    mode : {'train_eval', 'predict'}
        the mode of execution of the task to be executed: 'train_eval' to train
        the different parameters of the model using training data; 'predict' to
        generate predictions using previously trained parameters.

    Examples
    --------
    Extract training data from source data stores and save it into a staging
    database:

    >>> main('source', 'train_eval')

    Read training data from a staging database and use it to extract
    preprocessing parameters and, after that, preprocess it:

    >>> main('preprocess', 'train_eval')

    Read preprocessed training data and use it to train a classification model:

    >>> main('model', 'train_eval')
    """

    try:
        logger.info(f"Executing {task} task on {mode} mode")
        tasks[task][mode]()
    except Exception:
        logger.error(f"Task {task} failed")
        raise


@click.command()
@click.option(
    "--task",
    type=click.Choice(list(tasks.keys())),
    required=True,
    help="Name of task to execute",
)
@click.option(
    "--mode",
    type=click.Choice(mode),
    required=True,
    help="Mode of execution of the task",
)
def main_cli(task: str, mode: str):
    """
    Calls main() function. This function is weapped with CLI, so it can be
    passed with arguments from command line.

    main() and main_cli() are sepparated as main_cli() cannot be imported due
    to CLI decorators.
    """
    main(task, mode)
