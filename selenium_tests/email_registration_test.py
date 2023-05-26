import time

from datas import users
from datas.password import PASSWORD_LIST
from drivers import browser_initializer
from xpaths.xpaths import EmailPageXpaths
from xpaths.xpaths import MainPageXpaths


driver = browser_initializer.init_browser_on_main_page_and_return_driver()


def _put_password_and_makes_screenshot(passw):
    password_input_field = driver.find_element('xpath', EmailPageXpaths.REGISTRATION_PASSWORD_FIELD)
    password_input_field.send_keys(passw.password)
    time.sleep(2)
    driver.get_screenshot_as_file("screens\\" + passw.name + ".png")

time.sleep(1)

e_mail_button = driver.find_element('xpath', MainPageXpaths.EMAIL_WEBSITE_LINK)
e_mail_button.click()
time.sleep(1)


e_mail_registration = driver.find_element('xpath', EmailPageXpaths.EMAIL_REGISTRATION)
e_mail_registration.click()
time.sleep(1)

registration_login = driver.find_element('xpath', EmailPageXpaths.REGISTRATION_LOGIN)
registration_login.send_keys(users.OCCUPIED_USER.name)
time.sleep(1)

submit_login = driver.find_element('xpath', EmailPageXpaths.REGISTRATION_SUBMIT_BUTTON)
submit_login.click()
time.sleep(3)

driver.get_screenshot_as_file('screens\\occupied_user.png')

registration_login = driver.find_element('xpath', EmailPageXpaths.REGISTRATION_LOGIN)
registration_login.clear()
registration_login.send_keys(users.ACCEPTABLE_USER.name)
time.sleep(1)

submit_login = driver.find_element('xpath', EmailPageXpaths.REGISTRATION_SUBMIT_BUTTON)
submit_login.click()
time.sleep(3)

driver.get_screenshot_as_file('screens\\acceptable_user.png')


for test_password in PASSWORD_LIST:
    _put_password_and_makes_screenshot(test_password)
