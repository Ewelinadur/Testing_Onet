import time

from datas import password
from datas import users

from pages.email_page import EmailPage


def test_a():
    email_login = EmailPage()
    email_login.open_login_to_email_form()
    login_field = email_login.find_login_field()
    login_field.send_keys(users.FULL_USER_NAME.name)

    password_field = email_login.find_password_field()
    password_field.send_keys(password.PASSWORD_7_SMALL_LETTERS_PLUS_1_NUMBER.password)

    email_login.submit()

    time.sleep(1)

    email_login.make_screenshot('not_allowed_login.png')

    assert email_login.login_to_email_accepted()
