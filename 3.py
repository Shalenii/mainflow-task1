def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial_recursive(n - 1)
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial_recursive(number)}")
