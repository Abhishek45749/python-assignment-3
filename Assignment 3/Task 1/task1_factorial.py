# task1_factorial.py

def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Sample call
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
