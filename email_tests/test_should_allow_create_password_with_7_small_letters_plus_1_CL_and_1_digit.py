import time

from datas import password, users
from pages.password_page import PasswordPage


def test_should_allow_create_password_with_7_small_letters_plus_1_cl_and_1_digit():
    password_page = PasswordPage()
    registration_login_form = password_page.open_email_registration_form()
    registration_login_form.send_keys(users.ACCEPTABLE_USER.name)
    time.sleep(1)
    password_page.submit()

    registration_password_form = password_page.find_registration_password_field()
    registration_password_form.send_keys(password.PASSWORD_7_SMALL_LETTERS_PLUS_1_CAPITAL_LETTER_AND_1_DIGIT.password)

    registration_repassword_field = password_page.find_email_repassword_field()
    registration_repassword_field.send_keys(password.PASSWORD_7_SMALL_LETTERS_PLUS_1_CAPITAL_LETTER_AND_1_DIGIT.password)
    time.sleep(1)

    password_page.make_screenshot('password_1_cl_and_1_digit.png')
    password_page.submit()
    time.sleep(3)

    password_page.make_screenshot('phone_website.png')

    assert password_page.phone_website_is_opened()

