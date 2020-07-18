import time
import logging

from insta_utils.base_page import BasePage
from insta_utils.ig_pages.login_page_locators import InstagramLoginPageLocators


class InstagramLoginPage(BasePage):

    login_locators = InstagramLoginPageLocators

    def get_login_page(self):
        url = "https://www.instagram.com/"
        self.get_page(url)
        self.wait_for_browser_title("Instagram")

    def input_username(self, username):
        self.find_element(self.login_locators.USERNAME_TEXT_FIELD).send_keys(username)

    def input_password(self, password):
        self.find_element(self.login_locators.PASSWORD_TEXT_FIELD).send_keys(password)

    def click_login_button(self):
        self.find_element(self.login_locators.LOGIN_BUTTON).click()
        self.wait_page_until_loading()

    def click_login_with_facebook(self):
        self.find_element(self.login_locators.FB_LOGIN_BUTTON).click()
        self.wait_page_until_loading()

    def check_login_error_alert_msg(self, exp_msg: str):
        alert_text = self.find_element(self.login_locators.LOGIN_ERROR_ALERT).text
        assert exp_msg == alert_text

    def verify_username_alert(self):
        self.check_login_error_alert_msg(self.login_locators.WRONG_USERNAME_ALERT_TEXT)

    def verify_password_alert(self):
        self.check_login_error_alert_msg(self.login_locators.WRONG_PASSWORD_ALERT_TEXT)

    def verify_search_bar_exist(self):
        for _ in range(self.implicitly_wait_timeout):
            search_bar_st = self.is_element_present(self.login_locators.SEARCH_BAR)
            logging.debug("Search bar status: %s", search_bar_st)
            if search_bar_st:
                break
            time.sleep(1)
            self.show_all_elements()
        else:
            raise TimeoutError("Verify search bar exist timeout.")
