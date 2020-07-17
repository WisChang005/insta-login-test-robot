import os
import yaml


def read_yaml_file(yaml_file: str) -> dict:
    with open(yaml_file, "r") as steam:
        yaml_config = yaml.safe_load(steam)
    return yaml_config


def read_config():
    config_path = os.environ["CONFIG_FILE"]
    return read_yaml_file(config_path)
