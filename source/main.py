import threading

from source.DivisibleByFive import divisible_by_five
from source.Palindrome_check import Integer


def main():
    # Read input from file
    with open('../Input_Data/DivisibleByFive.txt', 'r') as file:
        binary_numbers = file.read().split(',')

    # Binary no divisible by 5
    result_program1 = divisible_by_five(binary_numbers)
    print(f"Program 1 Output: {','.join(result_program1)}")
    #Palindrome
    with open('../Input_Data/Palindrome_Check.txt', 'r') as file:
        palindrome_input = file.read()
    n = Integer(int(palindrome_input))

    if n.is_palindrome():
        palindrome_result = "a palindrome"
    else:
        palindrome_result = "not a palindrome"

    output_message = f"Program 2 Output: {n.value} is {palindrome_result}"
    print(output_message)



if __name__ == "__main__":
    main()