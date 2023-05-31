class Password:
    def __init__(self, passw, name):
        self.password = passw
        self.name = name


PASSWORD_7_SMALL_LETTERS = Password('abcdefg', "7_letters")

PASSWORD_7_SMALL_LETTERS_PLUS_1_CAPITAL_LETTER = Password('abcdefgI', "1_capital")

PASSWORD_7_SMALL_LETTERS_PLUS_1_NUMBER = Password('abcdefg1', "1_number")

PASSWORD_7_SMALL_LETTERS_PLUS_1_SPECIAL_CHARACTER = Password('Abcdefg!', "1_special")

PASSWORD_7_SMALL_LETTERS_PLUS_1_CAPITAL_LETTER_AND_1_NUMBER = Password('abcdefgI1', "1_capital_number_and_1_number")
