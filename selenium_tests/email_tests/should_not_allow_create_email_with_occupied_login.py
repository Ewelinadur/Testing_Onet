import time

from datas import users
from selenium_tests.email_tests.email_page_helper import EmailPage

registration_form = EmailPage()
registration_login_form = registration_form.open_registration_form()
registration_login_form.send_keys(users.OCCUPIED_USER.name)
time.sleep(1)
registration_form.submit()
registration_form.make_screenshot('..\\screens\\occupied_user.png')

assert registration_form.email_occupied_message_is_present()

