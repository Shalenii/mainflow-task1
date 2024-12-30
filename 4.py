def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
def generate_fibonacci_recursive(n):
    if n <= 0:
        return "Please enter a positive integer."
    return [fibonacci_recursive(i) for i in range(n)]
num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = generate_fibonacci_recursive(num_terms)
print(f"The first {num_terms} numbers in the Fibonacci sequence are: {fibonacci_sequence}")
