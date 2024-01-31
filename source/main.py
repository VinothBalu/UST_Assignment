import threading

from source.DivisibleByFive import divisible_by_five
from source.Palindrome_check import Integer


def main():
    # Read input from file
    with open('../Input_Data/DivisibleByFive.txt', 'r') as file:
        binary_numbers = file.read().split(',')

    # Program 1
    result_program1 = divisible_by_five(binary_numbers)
    print(f"Program 1 Output: {','.join(result_program1)}")

