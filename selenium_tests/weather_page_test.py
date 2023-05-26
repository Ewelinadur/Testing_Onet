import time

from drivers import browser_initializer
from xpaths.xpaths import WeatherPageXpaths

driver = browser_initializer.init_browser_on_main_page_and_return_driver()

weather_menu = driver.find_element('xpath', WeatherPageXpaths.WEATHER_MENU_BUTTON )
weather_menu.click()
time.sleep(1)

city_field = driver.find_element('xpath', WeatherPageXpaths.CITY_FIELD)
city_field.click()
city_field.clear()
city_field.send_keys('Kraków')
time.sleep(1)

top_label_in_city_list = driver.find_element('xpath', WeatherPageXpaths.TOP_LIST_BUTTON)
top_label_in_city_list.click()
time.sleep(1)

driver.get_screenshot_as_file('weatherafter.png')
time.sleep(3)

temperature_number = driver.find_element('xpath', WeatherPageXpaths.TEMPERATURE_NUMBER)
print(temperature_number.text)
print(type(temperature_number.text))

try:
    assert temperature_number.text.isnumeric() == True
except:
    driver.get_screenshot_as_file('minus temperature.png')
finally:
    print('po asercji')
