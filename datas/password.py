class Password:
    def __init__(self, passw, name):
        self.password = passw
        self.name = name


PASSWORD_7_LETTERS = Password('abcdefg', "7_letters")

PASSWORD_8_LETTERS = Password('abcdefgh', "8_letters")

PASSWORD_1_CAPITAL_LETTER = Password('Abcdefgh', "1_capital")

PASSWORD_1_NUMBER = Password('Abcdefgh1', "1_number")

PASSWORD_1_SPECIAL_CHARACTER = Password('Abcdefgh1!', "1_special")

PASSWORD_LIST = [PASSWORD_7_LETTERS, PASSWORD_8_LETTERS, PASSWORD_1_CAPITAL_LETTER, PASSWORD_1_NUMBER, PASSWORD_1_SPECIAL_CHARACTER]