import time

from datas import users
from pages.email_page import EmailPage


def test_should_allow_create_email_with_accepted_login():
    registration_form = EmailPage()
    registration_login_form = registration_form.open_registration_form()
    registration_login_form.send_keys(users.ACCEPTABLE_USER.name)
    time.sleep(2)

    registration_form.submit()
    registration_form.make_screenshot('acceptable_user.png')

    assert registration_form.email_accepted_website_open()
