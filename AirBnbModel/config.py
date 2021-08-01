import yaml
import os
import logging.config

from box import Box

# Open and save configuration .yml on 
with open("configs/config.yml", "r") as ymlfile:
    cfg = Box(yaml.safe_load(ymlfile))


os.makedirs(cfg.base.path.logs, exist_ok=True)                                

if os.path.exists(cfg.base.path.log_config):
    with open(cfg.base.path.log_config, "r") as ymlfile:
        log_config = yaml.safe_load(ymlfile)

    #Set up the logger configuration
    logging.config.dictConfig(log_config)
else:
    raise FileNotFoundError(f"Log yaml configuration file not found in {cfg.base.path.log_config}")