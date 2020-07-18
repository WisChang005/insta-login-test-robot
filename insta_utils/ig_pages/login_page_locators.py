from selenium.webdriver.common.by import By


class InstagramLoginPageLocators:

    # locators
    USERNAME_TEXT_FIELD = (By.NAME, "username")
    PASSWORD_TEXT_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    FB_LOGIN_BUTTON = (By.XPATH, '//button[@class="sqdOP yWX7d    y3zKF     " and @type="button"]')
    LOGIN_ERROR_ALERT = (By.ID, "slfErrorAlert")
    SEARCH_BAR = (By.XPATH, "//div[@class=\"pbgfb Di7vw \" and @role=\"button\"]")

    # alert msg
    WRONG_USERNAME_ALERT_TEXT = ("The username you entered doesn't belong to an account. "
                                 "Please check your username and try again.")
    WRONG_PASSWORD_ALERT_TEXT = "Sorry, your password was incorrect. Please double-check your password."
