import unittest

from source.DivisibleByFive import divisible_by_five


class TestProgram1(unittest.TestCase):
    def test_divisible_by_five(self):
        binary_numbers = ["1010", "1001"]
        result = divisible_by_five(binary_numbers)
        self.assertEqual(result, ['1010'])

    def test_empty_input(self):
        binary_numbers = []
        result = divisible_by_five(binary_numbers)
        self.assertEqual(result, [])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            binary_numbers = ["", ""]
            divisible_by_five(binary_numbers)


if __name__ == '__main__':
    unittest.main()