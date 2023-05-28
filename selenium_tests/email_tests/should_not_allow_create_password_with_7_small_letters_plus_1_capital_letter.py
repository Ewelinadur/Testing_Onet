import time

from datas import password, users
from selenium_tests.email_tests.password_page_helper import PasswordPage


password_page = PasswordPage()
registration_login_form = password_page.open_email_registration_form()
registration_login_form.send_keys(users.ACCEPTABLE_USER.name)
time.sleep(3)

password_page.submit()

registration_password_field = password_page.find_registration_password_field()
registration_password_field.send_keys(password.PASSWORD_7_SMALL_LETTERS_PLUS_1_CAPITAL_LETTER.password)

registration_repassword_field = password_page.find_email_repassword_field()
registration_repassword_field.send_keys(password.PASSWORD_7_SMALL_LETTERS_PLUS_1_CAPITAL_LETTER.password)
time.sleep(1)

password_page.make_screenshot('..\\screens\\password_7_letters.png')

assert password_page.submit_button_is_disabled()

