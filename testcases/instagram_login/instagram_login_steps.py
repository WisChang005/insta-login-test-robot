# import time
# import logging

from insta_utils import file_util
from insta_utils.robot_data import RobotDataStore
from insta_utils.browser_drivers import browser_helper
from insta_utils.insta_pages.instagram_login_page import InstagramLoginPage


def setup_instagram_login_page(browser_type):
    browser_map = {
        "chrome": browser_helper.get_chrome_driver,
        "firefox": browser_helper.get_firefox_driver
    }
    if browser_type not in browser_map:
        raise ValueError("Browser type error")
    driver = browser_map[browser_type]()
    login_page_obj = InstagramLoginPage(driver)
    RobotDataStore.set_env_var("login_page_obj", login_page_obj)


def get_instagram_login_page():
    login_page = RobotDataStore.get_env_var("login_page_obj")
    login_page.get_login_page()


def close_instagram_login_page():
    login_page = RobotDataStore.get_env_var("login_page_obj")
    login_page.close_this_browser()


def type_correct_login_info():
    login_page = RobotDataStore.get_env_var("login_page_obj")
    username = file_util.read_config()["instagram_user"]
    password = file_util.read_config()["instagram_pwd"]
    login_page.input_username(username)
    login_page.input_password(password)


def click_login_button():
    login_page = RobotDataStore.get_env_var("login_page_obj")
    login_page.click_login_button()


def click_login_with_fb():
    login_page = RobotDataStore.get_env_var("login_page_obj")
    login_page.click_login_with_facebook()


def check_login_succeed():
    login_page = RobotDataStore.get_env_var("login_page_obj")
    login_page.wait_for_browser_title("Instagram")


def check_page_title(page_title):
    login_page = RobotDataStore.get_env_var("login_page_obj")
    login_page.wait_for_browser_title_by_partial(page_title)


def type_incorrect_login_info(incorrect_field: str):
    login_page = RobotDataStore.get_env_var("login_page_obj")
    if incorrect_field == "username":
        username = "wrong_username@gmail.com"
        password = file_util.read_config()["instagram_pwd"]

    if incorrect_field == "password":
        username = file_util.read_config()["instagram_user"]
        password = "wrong Passw0rd@"

    login_page.input_username(username)
    login_page.input_password(password)


def check_login_error_alert_msg(incorrect_field: str):
    login_page = RobotDataStore.get_env_var("login_page_obj")
    if incorrect_field == "username":
        exp_msg = "The username you entered doesn't belong to an account. Please check your username and try again."

    if incorrect_field == "password":
        exp_msg = "Sorry, your password was incorrect. Please double-check your password."
    login_page.check_login_error_alert_msg(exp_msg)
