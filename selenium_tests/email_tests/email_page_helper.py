import time

from selenium.common import NoSuchElementException

from drivers import browser_initializer
from xpaths.xpaths import EmailPageXpaths, MainPageXpaths


class EmailPage:
    def __init__(self):
        self.driver = browser_initializer.init_browser_on_main_page_and_return_driver()

    def put_password_and_makes_screenshot(self, password):
        password_input_field = self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_PASSWORD_FIELD)
        password_input_field.send_keys(password.password)
        time.sleep(2)
        self.driver.get_screenshot_as_file("screens\\" + password.name + ".png")

    def open_registration_form(self):
        e_mail_button = self.driver.find_element('xpath', MainPageXpaths.EMAIL_WEBSITE_LINK)
        e_mail_button.click()
        time.sleep(1)

        e_mail_registration = self.driver.find_element('xpath', EmailPageXpaths.EMAIL_REGISTRATION)
        e_mail_registration.click()
        time.sleep(1)

        registration_login_input = self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_LOGIN)
        return registration_login_input

    def submit_login(self):
        submit_login = self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_SUBMIT_BUTTON)
        submit_login.click()
        time.sleep(3)

    def make_screenshot(self, screenshot_path):
        print("Trying to save screenshot to " + screenshot_path)
        if self.driver.get_screenshot_as_file(screenshot_path):
            print("Screenshot saved successfully")
        else:
            print("Error during saving screenshot")

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
