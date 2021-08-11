"""
Loads .yml configuration files located on '/configs', and stores them into a
Box object, so it can be latter imported and accessed programmatically on
other scripts of the package.
"""

import logging.config
import os
from pathlib import Path

import yaml
from box import Box

# Absolute path of the Package -> Used to define the location of configs files
root_directory = Path(__file__).parents[1].absolute()

# Open and save configuration .yml
cfg_path = os.path.join(root_directory, "configs/config.yml")
with open(cfg_path, "r") as ymlfile:
    cfg = Box(yaml.safe_load(ymlfile))


# Configuration for the logger
log_path = os.path.join(root_directory, cfg.base.path.logs)
os.makedirs(log_path, exist_ok=True)

log_config_path = os.path.join(root_directory, cfg.base.path.log_config)
if os.path.exists(log_config_path):
    with open(log_config_path, "r") as ymlfile:
        log_config = yaml.safe_load(ymlfile)

    # Set up the logger configuration dict for logger -> logging file path
    # is modifyed to be set as absolute path
    handlers = log_config["handlers"]
    log_config["handlers"]["debug_file_handler"]["filename"] = os.path.join(
        root_directory, handlers["debug_file_handler"]["filename"]
    )
    log_config["handlers"]["info_file_handler"]["filename"] = os.path.join(
        root_directory, handlers["info_file_handler"]["filename"]
    )
    logging.config.dictConfig(log_config)
else:
    raise FileNotFoundError(
        f"Log yaml configuration file not found in {log_config_path}"
    )
