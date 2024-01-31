from DivisibleByFIve import divisible_by_five
from palindrome_check import Integer, Singleton
import threading

def main():
    # Read input from file
    with open('input_data/binary_numbers.txt', 'r') as file:
        binary_numbers = file.read().split(',')

    # Program 1
    result_program1 = divisible_by_five(binary_numbers)
    print(f"Program 1 Output: {','.join(result_program1)}")

    # Program 2
    n = Integer(121)
    print(f"Program 2 Output: {n.value} is {'a palindrome' if n.is_palindrome() else 'not a palindrome'}")

    # Program 2 - Singleton
    instance1 = Singleton()
    instance2 = Singleton()
    print(f"Are instances the same? {instance1 is instance2}")

if __name__ == "__main__":
    main()