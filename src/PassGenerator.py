import GenerateArray
import utils
import random

class PasswordGenerator:
    def __init__(self, length, include_uppercase, include_lowercase, include_numbers, include_special_characters):
        self._length = length
        self._include_uppercase = include_uppercase
        self._include_lowercase = include_lowercase
        self._include_numbers = include_numbers
        self._include_special_characters = include_special_characters

    def generate_password(self):
        array_pass = [None] * self._length

        if self._include_uppercase:
            upperArr = GenerateArray.generate_char_array('uppercase')
            randLocation = random.randint(0, self._length - 1)
            while array_pass[randLocation] is not None:
                randLocation = random.randint(0, self._length - 1)
            array_pass[randLocation] = random.choice(upperArr)

        if self._include_lowercase:
            lowerArr = GenerateArray.generate_char_array('lowercase')
            randLocation = random.randint(0, self._length - 1)
            while array_pass[randLocation] is not None:
                randLocation = random.randint(0, self._length - 1)
            array_pass[randLocation] = random.choice(lowerArr)

        if self._include_numbers:
            digitsArr = GenerateArray.generate_char_array('digits')
            randLocation = random.randint(0, self._length - 1)
            while array_pass[randLocation] is not None:
                randLocation = random.randint(0, self._length - 1)
            array_pass[randLocation] = random.choice(digitsArr)

        if self._include_special_characters:
            specCharArr = GenerateArray.generate_char_array('special characters')
            randLocation = random.randint(0, self._length - 1)
            while array_pass[randLocation] is not None:
                randLocation = random.randint(0, self._length - 1)
            array_pass[randLocation] = random.choice(specCharArr)

        for i in range(0, self._length):
            if array_pass[i] is None:
                randType = random.randint(0, 3)
                while array_pass[i] is None:
                    if randType == 0 and self._include_uppercase:
                        array_pass[i] = random.choice(upperArr)
                    elif randType == 1 and self._include_lowercase:
                        array_pass[i] = random.choice(lowerArr)
                    elif randType == 2 and self._include_numbers:
                        array_pass[i] = random.choice(digitsArr)
                    elif self._include_special_characters:
                        array_pass[i] = random.choice(specCharArr)
                    randType = random.randint(0, 3)

        str_pass = ''.join(array_pass)
        return str_pass

    def is_password_secure(self, password):
        if len(password) >= 6 and not utils.has_common_patterns(password):
            if self.get_include_uppercase() and not any(c.isupper() for c in password):
                return False
            if self.get_include_lowercase() and not any(c.islower() for c in password):
                return False
            if self.get_include_numbers() and not any(c.isdigit() for c in password):
                return False
            if self.get_include_special_characters() and all(c.isalnum() for c in password):
                return False
            return True
        else:
            return False

    # Getter and setter methods for instance variables
    def get_length(self):
        return self._length

    def set_length(self, length):
        if length >= 2:
            self._length = length
        else:
            raise ValueError("Length must be at least 2")

    def get_include_uppercase(self):
        return self._include_uppercase

    def set_include_uppercase(self, include_uppercase):
        self._include_uppercase = include_uppercase

    def get_include_lowercase(self):
        return self._include_lowercase

    def set_include_lowercase(self, include_lowercase):
        self._include_lowercase = include_lowercase

    def get_include_numbers(self):
        return self._include_numbers

    def set_include_numbers(self, include_numbers):
        self._include_numbers = include_numbers

    def get_include_special_characters(self):
        return self._include_special_characters

    def set_include_special_characters(self, include_special_characters):
        self._include_special_characters = include_special_characters
