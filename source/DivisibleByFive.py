def divisible_by_five(binary_numbers):
    result = []
    for num in binary_numbers:
        decimal_num = init(num, 2)
        if decimal_num % 5 == 0:
            result.append(num)
    return result