import time

from datas import password, users
from selenium_tests.email_tests.password_page_helper import PasswordPage


password_page = PasswordPage()
registration_login_form = password_page.open_email_registration_form()
registration_login_form.send_keys(users.ACCEPTABLE_USER.name)
time.sleep(1)
password_page.submit_login()

registration_password_form = password_page.find_email_password_form()
registration_password_form.send_keys(password.PASSWORD_1_SPECIAL_CHARACTER.password)

registration_password_form = password_page.find_email_password_form_2()
registration_password_form.send_keys(password.PASSWORD_1_SPECIAL_CHARACTER.password)
time.sleep(1)

password_page.make_screenshot('..\\screens\\password_1_special character.png')

assert not password_page.submit_button_is_disabled()

