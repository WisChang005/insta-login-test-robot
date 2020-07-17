import time
import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.wait = None
        self.driver = driver
        self.implicitly_wait_timeout = 15
        self.driver.implicitly_wait(15)
        self.set_explicit_wait_timeout(60)
        self.driver.maximize_window()

    def set_explicit_wait_timeout(self, timeout):
        self.wait = WebDriverWait(self.driver, timeout)

    def get_page(self, url):
        logging.info("Open URL -> %s", url)
        self.driver.get(url)

    def quit_driver(self):
        logging.info("Quit driver")
        self.driver.quit()

    def find_element(self, *locator):
        logging.debug("Find Element: %s", *locator)
        _element = self.wait.until(expected_conditions.presence_of_element_located(*locator))
        return _element

    def wait_for_browser_title(self, exp_title, timeout=60):
        for _ in range(timeout):
            logging.debug("Wait for browser title Exp: [%s], Act: [%s]", exp_title, self.driver.title)
            if self.driver.title == exp_title:
                break
            time.sleep(1)
        else:
            raise TimeoutError("Wait for browser title present timeout")

    def wait_for_browser_title_by_partial(self, partial_tital, timeout=60):
        for _ in range(timeout):
            logging.debug("Wait for browser title Exp: [%s], Act: [%s]", partial_tital, self.driver.title)
            if partial_tital in self.driver.title:
                break
            time.sleep(1)
        else:
            raise TimeoutError("Wait for browser title present timeout")

    def is_element_present(self, *locator):
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element(*locator)
            return True
        except Exception:
            return False
        finally:
            self.driver.implicitly_wait(self.implicitly_wait_timeout)

    def is_page_load_complete(self):
        js_state = ''
        retry_times = 0
        while js_state == '':
            try:
                js_state = self.driver.execute_script('return window.document.readyState;')
            except Exception:
                js_state = ''
                retry_times += 1
                time.sleep(0.5)

            if retry_times > 5:
                js_state = 'complete'
                break

        return js_state == 'complete'

    def wait_page_until_loading(self):
        """ Wait page until loading """
        logging.info('>>> Wait for page until loading...')
        wait_time = 0.2
        start_t = time.time()

        load_st_timeout = 0
        while self.is_page_load_complete():
            logging.debug('Wait page status changed...')
            time.sleep(wait_time)
            load_st_timeout += 1
            if load_st_timeout > 15:  # 15 times (15 * 0.2 = 3 sec)
                logging.debug('Page status not changed')
                break
        else:
            logging.info('Start Page to loading')

        if not self.is_page_load_complete():
            # wait page loading after 15 sec get timeout
            logging.info('Wait page loading...')
            try:
                WebDriverWait(self.driver, 60).until(lambda driver: self.is_page_load_complete())
            except Exception:
                raise Exception("WAIT_PAGE_LOADING_TIMEOUT")
            else:
                logging.info('Wait page loading complete!')

        end_t = time.time()
        elapsedtime = round((end_t - start_t), 3)
        logging.info("<<< Wait page loading spend time %s", elapsedtime)
