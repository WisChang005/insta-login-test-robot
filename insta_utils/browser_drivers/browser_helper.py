import os
import platform
import pathlib

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options

from insta_utils.config_helper import ConfigHelper


def get_this_path():
    return str(pathlib.Path(__file__).parent.absolute())


def get_chrome_driver():
    driver_bin_map = {
        "Windows": "chromedriver.exe",
        "Darwin": "chromedriver",
        "Linux": "chromedriver"
    }
    driver_path = os.path.join(get_this_path(), driver_bin_map[platform.system()])
    chrome_options = Options()
    chrome_options.add_argument("--lang=en")
    driver = Chrome(executable_path=driver_path, service_args=["--verbose"], options=chrome_options)
    return driver


def get_firefox_driver():
    driver_bin_map = {
        "Windows": "geckodriver.exe",
        "Darwin": "geckodriver",
        "Linux": "geckodriver"
    }
    driver_path = os.path.join(get_this_path(), driver_bin_map[platform.system()])
    firefox_bin = ConfigHelper().get_firefix_binary_path()
    driver = Firefox(firefox_binary=firefox_bin, executable_path=driver_path)
    return driver
