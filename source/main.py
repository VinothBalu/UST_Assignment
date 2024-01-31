import threading

from source.DivisibleByFive import divisible_by_five
from source.Palindrome_check import Singleton,Integer


def main():
    # Read input from file
    with open('../Input_Data/DivisibleByFive.txt', 'r') as file:
        binary_numbers = file.read().split(',')

    # Program 1
    result_program1 = divisible_by_five(binary_numbers)
    print(f"Program 1 Output: {','.join(result_program1)}")

    with open('../Input_Data/Palindrome_Check.txt', 'r') as file:
        palindrome_input = file.read()
    n = Integer(int(palindrome_input))
    print(f"Program 2 Output: {n.value} is {'a palindrome' if n.is_palindrome() else 'not a palindrome'}")



if __name__ == "__main__":
    main()