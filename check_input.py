import string



class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, _char, _index):
        self._char = _char
        self._index = _index
    def __str__(self):
        return f"""The username contains an illegal character
                character "{self._char}" at index {self._index}"""

class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"

class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"

class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"

class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"

class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"

class PasswordMissingCharacterUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super(PasswordMissingCharacterUppercase, self).__str__() + " (Uppercase)"

class PasswordMissingCharacterLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super(PasswordMissingCharacterLowercase, self).__str__() + " (Lowercase)"
class PasswordMissingCharacterDigit(PasswordMissingCharacter):
    def __str__(self):
        return super(PasswordMissingCharacterDigit, self).__str__() + " (Digit)"

class PasswordMissingCharacterSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super(PasswordMissingCharacterSpecial, self).__str__() + " (Special)"


















print(string.punctuation)


def check_input(username, password):
    for char in username:
        if not char.isnumeric() and not char.isalpha() and char != "_":
            raise UsernameContainsIllegalCharacter(char,username.index(char))
            return
    lower = False
    uper = False
    num = False
    spec = False
    for char in password:
        if char.islower():
            lower = True
        elif char.isnumeric():
            num =True
        elif char.isupper():
            uper = True
        elif char in string.punctuation:
            spec = True
        else:
            pass
    if len(username) < 3:
        raise UsernameTooShort
    elif len(username) > 16:
        raise UsernameTooLong
    elif len(password) < 8:
        raise PasswordTooShort
    elif len(password) > 40:
        raise PasswordTooLong
    elif not uper:
        raise PasswordMissingCharacterUppercase
    elif not lower:
        raise PasswordMissingCharacterLowercase
    elif not num:
        raise PasswordMissingCharacterDigit
    elif not spec:
        raise PasswordMissingCharacterSpecial
    else:
        print("OK")

try:
    check_input("1", "2")
except Exception as e:
    print(e)
try:
    check_input("0123456789ABCDEFG", "2")
except Exception as e:
    print(e)
try:
    check_input("A_a1.", "12345678")
except Exception as e:
    print(e)
try:
    check_input("A_1", "2")
except Exception as e:
    print(e)
try:
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
except Exception as e:
    print(e)
try:
    check_input("A_1", "abcdefghijklmnop")
except Exception as e:
    print(e)
try:
    check_input("A_1", "ABCDEFGHIJLKMNOP")
except Exception as e:
    print(e)
try:
    check_input("A_1", "ABCDEFGhijklmnop")
except Exception as e:
    print(e)
try:
    check_input("A_1", "4BCD3F6h1jk1mn0p")
except Exception as e:
    print(e)
try:
    check_input("A_1", "4BCD3F6.1jk1mn0p")
except Exception as e:
    print(e)















