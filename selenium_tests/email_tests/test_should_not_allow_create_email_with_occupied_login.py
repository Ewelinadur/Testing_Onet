import time

from datas import users
from pages.email_page import EmailPage


def test_should_not_allow_create_email_with_occupied_login():
    email_page = EmailPage()
    registration_login_form = email_page.open_registration_form()
    registration_login_form.send_keys(users.OCCUPIED_USER.name)
    time.sleep(1)
    email_page.submit()
    email_page.make_screenshot('occupied_user.png')

    assert email_page.email_occupied_message_is_present()
