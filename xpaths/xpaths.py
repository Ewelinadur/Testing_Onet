class MainPageXpaths:
    EMAIL_WEBSITE_LINK = "//a[@href='https://poczta.onet.pl/']"
    ACCEPT_COOKIES_BUTTON = "//button[contains(@aria-label,'accept')]"

class WeatherPageXpaths:
    WEATHER_MENU_BUTTON = '//div[contains(@class, "Weather_weatherCell")][1]//span[contains(@class, "Weather_label")]'
    CITY_FIELD = '//input[contains(@class, "LocationBrowser_search")]'
    TOP_LIST_BUTTON = '//div[contains(@class, "LocationBrowser_location_")]'
    TEMPERATURE_NUMBER = '//div[contains(@class, "Weather_temperature")]'

class EmailPageXpaths:
    EMAIL_REGISTRATION_BUTTON = "//a[contains(@href, 'register')]"

    REGISTRATION_LOGIN_FIELD = "//input[@name='alias']"
    SUBMIT_BUTTON = "//button[@type='submit']"
    EMAIL_OCCUPIED_MESSAGE = "//div[contains(text(), 'Niestety adres')]"
    EMAIL_ACCEPTED_WEBSITE = "//h2[contains(text(), 'Ustaw hasło')]"
    REGISTRATION_PASSWORD_FIELD = "//input[@name='newPassword']"
    REGISTRATION_REPASSWORD_FIELD = "//input[@name='rePassword']"
    PASSWORD_NOT_ACCEPTED_MESSAGE = "//div[contains(text(), 'Hasło musi zawierać')]"
    REGISTRATION_PASSWORD_PHONE_PAGE = "//h2[contains(text(), 'Podaj numer')]"
    EMAIL_FIELD = "//input[@type='email']"
    PASSWORD_FIELD = "//input[@type='password']"
    WRONG_EMAIL_OR_PASSWORD_MESSAGE = "//div[contains(text(), 'Nieprawidłowy')]"
    REGISTRATION_SUBMIT_BUTTON_DISABLED = "//button[@disabled]"

