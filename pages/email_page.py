import time

from selenium.common import NoSuchElementException

from drivers import browser_initializer
from helpers.screenshot_helper import ScreenshotMaker
from xpaths.xpaths import EmailPageXpaths, MainPageXpaths


class EmailPage:
    def __init__(self):
        self.driver = browser_initializer.init_browser_on_main_page_and_return_driver()
        self.screenshot_maker = ScreenshotMaker(self.driver)

    def open_registration_form(self):
        email_button = self.driver.find_element('xpath', MainPageXpaths.EMAIL_WEBSITE_LINK)
        email_button.click()
        time.sleep(1)

        email_registration_button = self.driver.find_element('xpath', EmailPageXpaths.EMAIL_REGISTRATION_BUTTON)
        email_registration_button.click()
        time.sleep(1)

        return self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_LOGIN_FIELD)

    def submit(self):
        submit_button = self.driver.find_element('xpath', EmailPageXpaths.SUBMIT_BUTTON)
        submit_button.click()
        time.sleep(1)

    def make_screenshot(self, screenshot_path):
        self.screenshot_maker.make_screenshot(screenshot_path)

    def email_occupied_message_is_present(self):
        try:
            self.driver.find_element('xpath', EmailPageXpaths.EMAIL_OCCUPIED_MESSAGE)
            return True
        except NoSuchElementException:
            return False

    def email_accepted_website_open(self):
        try:
            self.driver.find_element('xpath', EmailPageXpaths.EMAIL_ACCEPTED_WEBSITE)
            return True
        except NoSuchElementException:
            return False

    def open_login_to_email_form(self):
        email_button = self.driver.find_element('xpath', MainPageXpaths.EMAIL_WEBSITE_LINK)
        email_button.click()
        time.sleep(1)
        return email_button

    def find_login_field(self):
        login_input = self.driver.find_element('xpath', EmailPageXpaths.EMAIL_FIELD)
        login_input.clear()
        return login_input

    def find_password_field(self):
        password_input = self.driver.find_element('xpath', EmailPageXpaths.PASSWORD_FIELD)
        password_input.clear()
        return password_input

    def login_to_email_not_accepted(self):
        if self.driver.find_element('xpath', EmailPageXpaths.WRONG_EMAIL_OR_PASSWORD_MESSAGE):
            return True
        else:
            return False


