
class Integer:
    def __init__(self, value):
        self.value = value

    def is_palindrome(self):
        return str(self.value) == str(self.value)[::-1]

# Another class to create single instance
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
