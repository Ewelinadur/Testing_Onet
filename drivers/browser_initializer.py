import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from urls.urls import MAIN_WEBSITE_URL, EMAIL_WEBSITE_URL
from xpaths.xpaths import MainPageXpaths


def init_browser_on_url_and_return_driver(url):
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(2)

    cookies_button = driver.find_element('xpath', MainPageXpaths.ACCEPT_COOKIES_BUTTON)
    cookies_button.click()
    time.sleep(1)
    return driver


def init_browser_on_main_page_and_return_driver():
    return init_browser_on_url_and_return_driver(MAIN_WEBSITE_URL)


def init_email_browser_and_return_driver():
    return init_browser_on_url_and_return_driver(EMAIL_WEBSITE_URL)
