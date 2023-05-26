import time

from selenium.common import NoSuchElementException
from xpaths.xpaths import EmailPageXpaths
from drivers import browser_initializer


class PasswordPage:
    def __init__(self):
        self.driver = browser_initializer.init_email_browser_and_return_driver()

    def open_email_registration_form(self):
        e_mail_registration = self.driver.find_element('xpath', EmailPageXpaths.EMAIL_REGISTRATION)
        e_mail_registration.click()
        time.sleep(1)

        registration_login_input = self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_LOGIN)
        return registration_login_input

    def submit_login(self):
        submit_login = self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_SUBMIT_BUTTON)
        submit_login.click()
        time.sleep(3)

    def find_email_password_form(self):
        registration_password_input = self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_PASSWORD_FIELD)
        return registration_password_input

    def find_email_password_form_2(self):
        registration_password_input = self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_PASSWORD_FIELD_2)
        return registration_password_input

    def make_screenshot(self, screenshot_path):
        if self.driver.get_screenshot_as_file(screenshot_path):
            print("Screenshot saved successfully")
        else:
            print("Error during saving screenshot")

    def weak_password_message_is_present(self):
        try:
            self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_PASSWORD_MESSAGE)
            return True
        except NoSuchElementException:
            return False

    def submit_button_is_disabled(self):
        try:
            self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_SUBMIT_BUTTON_DISABLED)
            return True
        except NoSuchElementException:
            return False

    def password_accepted_website_open(self):
        try:
            self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_PASSWORD_PHONE_PAGE)
            return True
        except NoSuchElementException:
            return False