import time

from datas import users
from selenium_tests.email_tests.email_page_helper import EmailPage

email_page = EmailPage()
registration_login_form = email_page.open_registration_form()
registration_login_form.send_keys(users.ACCEPTABLE_USER.name)
time.sleep(2)

email_page.submit_login()
email_page.make_screenshot('..\\screens\\ acceptable_user.png')

assert email_page.email_accepted_website_open()




