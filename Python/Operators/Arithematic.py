# ---- Arithmetic Operators in Python ----

# Basic Arithmetic Operators:
# + : Addition
# - : Subtraction
# * : Multiplication
# / : Division (returns a float)
# % : Modulus (returns the remainder)
# ** : Exponentiation (raises a number to a power)
# // : Floor Division (division that returns the largest integer)

# Example 1: Basic arithmetic operations with two numbers

a, b = 10, 5  # Assigning values 10 and 5 to variables a and b

# Performing different arithmetic operations
print("Addition is ", a + b)           # Output: 15 (10 + 5)
print("Subtraction is ", a - b)        # Output: 5 (10 - 5)
print("Multiplication is ", a * b)     # Output: 50 (10 * 5)
print("Division is ", a / b)           # Output: 2.0 (10 / 5, gives float)
print("Modulus (remainder) is ", a % b)  # Output: 0 (10 % 5, no remainder)
print("Power is ", a ** b)             # Output: 100000 (10^5)
print("Floor division is ", a // b)    # Output: 2 (Integer division, rounds down)

# ---- Compound Assignment Operators ----

# Example 2: Using compound assignment operators with variables

x, y = 5, 15  # Assigning values 5 and 15 to variables x and y

# Compound assignment operators modify the value of x based on an operation with y

x += y  # Equivalent to: x = x + y
print(x)  # Output: 20 (5 + 15)

x -= y  # Equivalent to: x = x - y
print(x)  # Output: 5 (20 - 15)

x *= y  # Equivalent to: x = x * y
print(x)  # Output: 75 (5 * 15)
