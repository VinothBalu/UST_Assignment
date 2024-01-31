import unittest
from Palindrome_check import Integer

class TestProgram2(unittest.TestCase):
    def test_is_palindrome(self):
        n = Integer(121)
        result = n.is_palindrome()
        self.assertTrue(result)

    def test_invalid_input(self):
        n = Integer("ABC")
        result = n.invalid_input()
        self.assertFalse(result)  # Use assertFalse for checking invalid input

if __name__ == '__main__':
    unittest.main()
