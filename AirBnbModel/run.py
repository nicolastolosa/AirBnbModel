import click
import logging
from AirBnbModel.source.run import main as source_main
from AirBnbModel.preprocess.run import main as preprocess_main
from AirBnbModel.model.run import main as model_main


logger = logging.getLogger(__name__)



tasks = {
    "source": source_main,
    "preprocess": preprocess_main,
    "model": model_main
}
mode = ["train_eval", "predict"]



@click.command()
@click.option(
    "--task",
    type=click.Choice(tasks.keys()),
    required=True,
    help="Name of task to execute",
)
@click.option(
    "--mode",
    type=click.Choice(mode),
    required=True,
    help="Mode of execution of the task",
)
def main(task, mode):
    try:
        logger.info(f"Executing {task} task on {mode} mode")
        tasks[task](mode)
    except:
        logger.error(f"Task {task} failed")
        raise