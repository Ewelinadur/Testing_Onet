import time
from selenium import webdriver
from urls.urls import MAIN_WEBSITE_URL, EMAIL_WEBSITE_URL
from xpaths.xpaths import MainPageXpaths


def init_browser_on_main_page_and_return_driver():
    return init_browser_on_url_and_return_driver(MAIN_WEBSITE_URL)


def init_browser_on_url_and_return_driver(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)

    cookies_button = driver.find_element('xpath', MainPageXpaths.ACCEPT_COOKIES_BUTTON)
    cookies_button.click()
    time.sleep(1)
    return driver


def init_email_browser_and_return_driver():
    return init_browser_on_url_and_return_driver(EMAIL_WEBSITE_URL)
