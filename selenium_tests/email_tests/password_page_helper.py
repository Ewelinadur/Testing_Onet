import time

from selenium.common import NoSuchElementException
from xpaths.xpaths import MainPageXpaths, EmailPageXpaths
from drivers import browser_initializer


class PasswordPage:
    def __init__(self):
        self.driver = browser_initializer.init_email_browser_and_return_driver()

    def open_email_registration_form(self):
        email_registration_button = self.driver.find_element('xpath', EmailPageXpaths.EMAIL_REGISTRATION_BUTTON)
        email_registration_button.click()
        time.sleep(1)

        return self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_LOGIN_FIELD)

    # def find_and_clear_registration_login_field(self):
    #     registration_login_field = self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_LOGIN_FIELD)
    #     registration_login_field.clear()
    #     return registration_login_field

    def submit(self):
        submit_button = self.driver.find_element('xpath', EmailPageXpaths.SUBMIT_BUTTON)
        submit_button.click()
        time.sleep(1)

    def find_registration_password_field(self):
        registration_password_field = self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_PASSWORD_FIELD)
        registration_password_field.clear()
        return registration_password_field

    def find_email_repassword_field(self):
        registration_repassword_field = self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_REPASSWORD_FIELD)
        registration_repassword_field.clear()
        return registration_repassword_field

    def make_screenshot(self, screenshot_path):
        if self.driver.get_screenshot_as_file(screenshot_path):
            print("Screenshot saved successfully")
        else:
            print("Error during saving screenshot")

    def weak_password_message_is_present(self):
        try:
            self.driver.find_element('xpath', EmailPageXpaths.PASSWORD_NOT_ACCEPTED_MESSAGE)
            return True
        except NoSuchElementException:
            return False

    def submit_button_is_disabled(self):
        try:
            self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_SUBMIT_BUTTON_DISABLED)
            return True
        except NoSuchElementException:
            return False

    def phone_website_is_opened(self):
        try:
            self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_PASSWORD_PHONE_PAGE)
            return True
        except NoSuchElementException:
            return False

