import time

from selenium.common import NoSuchElementException

from drivers import browser_initializer
from helpers.screenshot_helper import ScreenshotMaker
from xpaths.xpaths import EmailPageXpaths


class PasswordPage:
    def __init__(self):
        self.driver = browser_initializer.init_email_browser_and_return_driver()
        self.screenshot_maker = ScreenshotMaker(self.driver)

    def open_email_registration_form(self):
        email_registration_button = self.driver.find_element('xpath', EmailPageXpaths.EMAIL_REGISTRATION_BUTTON)
        email_registration_button.click()
        time.sleep(1)

        return self.driver.find_element('xpath', EmailPageXpaths.REGISTRATION_LOGIN_FIELD)

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
        self.screenshot_maker.make_screenshot(screenshot_path)

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

    # def verify_correct_color_of_submit_button
    #     try:
    #         self.driver.find_element(By.type('submit'))
    #
    #
    #        WebElement t = driver.findElement(By.tagName("h1"));
    #   //obtain color in rgba
    #   String s = t.getCssValue("color");
    #   // convert rgba to hex
    #   String c = Color.fromString(s).asHex();
    #   System.out.println("Color is :" + s);
    #   System.out.println("Hex code for color:" + c);
    #   driver.quit();
