import time

from datas import password, users
from pages.password_page import PasswordPage

def test_should_not_allow_create_password_with_7_small_letters_plus_1_capital_letter():
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

    password_page.make_screenshot('password_7_letters_plus_1_cl.png')

    assert password_page.submit_button_is_disabled()

