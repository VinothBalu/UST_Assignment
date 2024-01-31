import unittest
from Palindrome_check import Integer

class TestProgram2(unittest.TestCase):
    def test_is_palindrome(self):
        n = Integer(121)
        result = n.is_palindrome()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
