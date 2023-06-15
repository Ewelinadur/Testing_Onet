class MainPageXpaths:
    EMAIL_WEBSITE_LINK = "//a[@href='https://poczta.onet.pl/']"
    ACCEPT_COOKIES_BUTTON = "//button[contains(@aria-label,'accept')]"

class EmailPageXpaths:
    EMAIL_REGISTRATION_BUTTON = "//a[contains(@href, 'register')]"
    REGISTRATION_LOGIN_FIELD = "//input[@name='alias']"
    SUBMIT_BUTTON = "//button[@type='submit']"
    EMAIL_OCCUPIED_MESSAGE = "//div[contains(text(), 'Niestety adres')]"
    EMAIL_ACCEPTED_WEBSITE = "//h2[contains(text(), 'Ustaw hasło')]"
    REGISTRATION_PASSWORD_FIELD = "//input[@name='newPassword']"
    REGISTRATION_REPASSWORD_FIELD = "//input[@name='rePassword']"
    PASSWORD_NOT_ACCEPTED_MESSAGE = "//div[contains(text(), 'Hasło musi zawierać')]"
    REGISTRATION_PASSWORD_PHONE_PAGE = "//label[contains(text(), 'Numer telefonu')]"
    EMAIL_FIELD = "//input[@type='email']"
    PASSWORD_FIELD = "//input[@type='password']"
    WRONG_EMAIL_OR_PASSWORD_MESSAGE = "//div[contains(text(), 'Nieprawidłowy email lub hasło')]"
    REGISTRATION_SUBMIT_BUTTON_DISABLED = "//button[@disabled]"
    ACTIVE_ICON_OF_SMALL_LETTERS = "//i[@data-testid='icon')]"

