class Integer:
    def __init__(self, value):
        self.value = value

    def is_palindrome(self):
        return str(self.value) == str(self.value)[::-1]
