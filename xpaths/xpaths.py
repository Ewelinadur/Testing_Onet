class MainPageXpaths:
    EMAIL_WEBSITE_LINK = "//a[@href='https://poczta.onet.pl/']"
    ACCEPT_COOKIES_BUTTON = "//button[contains(@aria-label,'accept')]"

class WeatherPageXpaths:
    WEATHER_MENU_BUTTON = '//div[contains(@class, "Weather_weatherCell")][1]//span[contains(@class, "Weather_label")]'
    CITY_FIELD = '//input[contains(@class, "LocationBrowser_search")]'
    TOP_LIST_BUTTON = '//div[contains(@class, "LocationBrowser_location_")]'
    TEMPERATURE_NUMBER = '//div[contains(@class, "Weather_temperature")]'

class EmailPageXpaths:
    EMAIL_REGISTRATION = "//a[contains(@href, 'register')]"
    REGISTRATION_LOGIN = "//input[@name='alias']"
    REGISTRATION_SUBMIT_BUTTON = "//button[@type='submit']"
    REGISTRATION_SUBMIT_BUTTON_DISABLED = "//button[@disabled]"
    REGISTRATION_PASSWORD_FIELD = "//input[@name='newPassword']"
    REGISTRATION_PASSWORD_FIELD_2 = "//input[@name='rePassword']"
    REGISTRATION_PASSWORD_MESSAGE = "//div[contains(text(), 'Hasło musi zawierać')]"
    #REGISTRATION_PASSWORD_SUBMIT_BUTTON = "//button[@type='submit']"
    EMAIL_OCCUPIED_MESSAGE = "//div[contains(text(), 'Niestety adres')]"
    EMAIL_ACCEPTED_WEBSITE = "//h2[contains(text(), 'Ustaw hasło')]"
    REGISTRATION_PASSWORD_PHONE_PAGE = "//h2[contains(text(), 'Podaj numer')]"

