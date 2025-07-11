# task2_math_module.py

import math

try:
    number = float(input("Enter a number: "))

    if number <= 0:
        print("For logarithm, please enter a number greater than 0.")
    else:
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)

        print(f"Square root of {number}: {square_root}")
        print(f"Natural logarithm of {number}: {natural_log}")
        print(f"Sine of {number} (radians): {sine_value}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
