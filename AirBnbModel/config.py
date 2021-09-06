"""
Loads .yml configuration files located on '/configs', and stores them into a
Box object, so it can be latter imported and accessed programmatically on
other scripts of the package.
"""

import logging.config
import os

import yaml
from box import Box

# Open and save configuration .yml
cfg_path = "configs/config.yml"
with open(cfg_path, "r") as ymlfile:
    cfg = Box(yaml.safe_load(ymlfile))

# Configuration for the logger
log_path = cfg.base.path.logs
os.makedirs(log_path, exist_ok=True)

# log_config_path = os.path.join(root_directory, cfg.base.path.log_config)
log_config_path = cfg.base.path.log_config
if os.path.exists(log_config_path):
    with open(log_config_path, "r") as ymlfile:
        log_config = yaml.safe_load(ymlfile)

    logging.config.dictConfig(log_config)
else:
    raise FileNotFoundError(
        f"Log yaml configuration file not found in {log_config_path}"
    )
