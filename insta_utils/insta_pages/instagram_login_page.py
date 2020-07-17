from selenium.webdriver.common.by import By

from insta_utils.base_page import BasePage


class InstagramLoginPage(BasePage):

    def get_login_page(self):
        url = "https://www.instagram.com/"
        self.get_page(url)
        self.wait_for_browser_title("Instagram")

    def input_username(self, username):
        locator = (By.NAME, "username")
        self.find_element(locator).send_keys(username)

    def input_password(self, password):
        locator = (By.NAME, "password")
        self.find_element(locator).send_keys(password)

    def click_login_button(self):
        locator = (By.XPATH, '//button[@type="submit"]')
        self.find_element(locator).click()
        self.wait_page_until_loading()

    def click_login_with_facebook(self):
        locator = (By.XPATH, '//button[@class="sqdOP yWX7d    y3zKF     " and @type="button"]')
        self.find_element(locator).click()
        self.wait_page_until_loading()

    def check_login_error_alert_msg(self, exp_msg: str):
        locator = (By.ID, "slfErrorAlert")
        alert_text = self.find_element(locator).text
        assert exp_msg == alert_text

    def close_this_browser(self):
        self.quit_driver()
