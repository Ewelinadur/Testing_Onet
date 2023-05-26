import time

from datas import users
from selenium_tests.email_tests.email_page_helper import EmailPage

email_page = EmailPage()
registration_login_form = email_page.open_registration_form()
registration_login_form.send_keys(users.OCCUPIED_USER.name)
time.sleep(1)
email_page.submit_login()
email_page.make_screenshot('..\\screens\\occupied_user.png')

#assert not email_page.email_occupied_message_is_present()

assert email_page.email_occupied_message_is_present()