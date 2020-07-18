import os

from insta_utils import file_util


class ConfigHelper:

    def __init__(self):
        self.config = self._read_config()

    @staticmethod
    def _read_config():
        config_path = os.environ["CONFIG_FILE"]
        return file_util.read_yaml_file(config_path)

    def get_firefix_binary_path(self):
        return self.config["firefox_binary"]

    def get_ig_username(self):
        return self.config["instagram_user"]

    def get_ig_password(self):
        return self.config["instagram_pwd"]
