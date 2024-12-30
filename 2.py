def check_odd_or_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
number = int(input("Enter a number: "))
result = check_odd_or_even(number)
print(f"The number {number} is {result}.")
