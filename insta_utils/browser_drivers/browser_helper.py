import os
import pathlib

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Firefox

from insta_utils import file_util


def get_this_path():
    return str(pathlib.Path(__file__).parent.absolute())


def get_chrome_driver():
    driver_path = os.path.join(get_this_path(), "chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument('--lang=en')
    driver = Chrome(executable_path=driver_path, service_args=["--verbose"], options=chrome_options)
    return driver


def get_firefox_driver():
    driver_path = os.path.join(get_this_path(), "geckodriver.exe")
    firefox_bin = file_util.read_config()["firefox_binary"]
    driver = Firefox(firefox_binary=firefox_bin, executable_path=driver_path)
    return driver
