def is_armstrong_number(n):
    """
    Check if a number is an Armstrong number.
    
    :param n: Integer to check
    :return: True if n is an Armstrong number, False otherwise
    """
    digits = str(n)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return n == sum_of_powers
print(is_armstrong_number(153))  # Output: True
print(is_armstrong_number(9474)) # Output: True
print(is_armstrong_number(123))  # Output: False
