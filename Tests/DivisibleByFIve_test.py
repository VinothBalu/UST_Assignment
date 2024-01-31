import unittest
from DivisibleByFive import divisible_by_five

class TestProgram1(unittest.TestCase):
    def test_divisible_by_five(self):
        binary_numbers = ["0100", "0011", "1010", "1001"]
        result = divisible_by_five(binary_numbers)
        self.assertEqual(result, ["1010"])
    def test_empty_input(self):
        binary_numbers = []
        result = divisible_by_five(binary_numbers)
        self.assertEqual(result, [])
    def test_invalid_input(self):
        binary_numbers = ["abcdefghijklmnopqrstuvwxyz"]
        result = divisible_by_five(binary_numbers)
        self.assertEqual(result, ["Invalid input"])
if __name__ == '__main__':
    unittest.main()
