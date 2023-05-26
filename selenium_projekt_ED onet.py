import time
from datas.users import OCCUPIED_USER

from selenium import webdriver


class XPaths:
    ACCEPT_COOKIES_BUTTON = '//*[@id="rasp_cmp"]/div/div[6]/button[2]'
    WEATHER_MENU_BUTTON = '//div[contains(@class, "Weather_weatherCell")][1]//span[contains(@class, "Weather_label")]'
    CITY_FIELD = '//input[contains(@class, "LocationBrowser_search")]'
    TOP_LIST_BUTTON = '//div[contains(@class, "LocationBrowser_location_")]'
    TEMPERATURE_NUMBER = '//div[contains(@class, "Weather_temperature")]'
    EMAIL_WEBSITE = "//a[@href='https://poczta.onet.pl/']"
    EMAIL_REGISTRATION = "//a[contains(@href, 'register')]"
    REGISTRATION_LOGIN = "//input[@name='alias']"
    REGISTRATION_SUBMIT_BUTTON = "//button[@type='submit']"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://onet.pl')
time.sleep(1)
cookies_button = driver.find_element('xpath', XPaths.ACCEPT_COOKIES_BUTTON)
cookies_button.click()
time.sleep(1)

# print('Nazwa strony to: ', driver.title)
# time.sleep(1)
# driver.get_screenshot_as_file('weatherbefore.png')
#
# weather_menu = driver.find_element('xpath', XPaths.WEATHER_MENU_BUTTON)
# weather_menu.click()
# time.sleep(1)
#
# city_field = driver.find_element('xpath', XPaths.CITY_FIELD)
#
# city_field.click()
# city_field.clear()
# city_field.send_keys('Kraków')
# time.sleep(1)
#
# top_label_in_city_list = driver.find_element('xpath', XPaths.TOP_LIST_BUTTON)
# top_label_in_city_list.click()
# time.sleep(1)
#
# driver.get_screenshot_as_file('weatherafter.png')
#
# time.sleep(3)
#
# temperature_number = driver.find_element('xpath', XPaths.TEMPERATURE_NUMBER)
# print(temperature_number.text)
#
#
# print(type(temperature_number.text))


# try:
#     assert temperature_number.text.isnumeric() == True
# except:
#     driver.get_screenshot_as_file('minus temperature.png')
# finally:
#     print('po asercji')


e_mail_button = driver.find_element('xpath', XPaths.EMAIL_WEBSITE)
e_mail_button.click()
time.sleep(1)


e_mail_registration = driver.find_element('xpath', XPaths.EMAIL_REGISTRATION)
e_mail_registration.click()
time.sleep(3)

registration_login = driver.find_element('xpath', XPaths.REGISTRATION_LOGIN)
registration_login.send_keys(OCCUPIED_USER.name)




# registration_login = driver.find_element('xpath', XPaths.REGISTRATION_LOGIN)
# registration_login.send_keys('ed3')


time.sleep(3)

driver.quit()