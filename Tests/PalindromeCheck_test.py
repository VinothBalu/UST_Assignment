import unittest

from source.Palindrome_check import Integer


class TestProgram2(unittest.TestCase):
    def test_is_palindrome(self):
        n = Integer(121)
        result = n.is_palindrome()
        self.assertTrue(result)

    def test_invalid_input(self):
        n = Integer(123)
        result = n.is_palindrome()
        self.assertFalse(result)  # Use assertFalse for checking invalid input

if __name__ == '__main__':
    unittest.main()