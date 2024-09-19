# # Syntax refers to the rules that define valid statements in a programming language.
# # Semantics refers to the meaning or sense of the code.
#
# # Simple print statements
# print("Hello Python")  # Double quotes
# print('Hello Python')  # Single quotes
#
# print("12345678")  # Printing numbers as a string
#
# # Variables and Basic Arithmetic
# a = 10
# b = 20
# d = "thirty"  # String
# c = a + b  # Addition of two integers
#
# print("The sum of a and b =", c)  # Output with comma-separated values
# print("The sum of", a, "and", b, "=", c)  # Printing multiple variables
#
# # Concatenation in strings (only works between strings)
# print("The sum of a and b = " + d)  # Concatenating with string
#
# # Example of concatenation with strings
# Colour = "Black"
# print("My Favourite Colour is " + Colour)
#
# # Input Example - Getting user input
# # Uncomment these lines if you want to use inputs
#
# # Name = input("What is your name: ")
# # print("My Name is " + Name)
#
# # String Concatenation vs Numeric Addition
# # By default, inputs are treated as strings
#
# # a = input("Enter the first number: ")  # Input is always a string
# # b = input("Enter the second number: ")
# # c = a + b  # This will concatenate the input as strings
# # print("Concatenated result:", c)  # For example, '2' + '3' = '23'
#
# # To perform addition, we need to convert the inputs to integers
# # a = int(input("Enter the first number: "))  # Convert input to integer
# # b = int(input("Enter the second number: "))
# # c = a + b  # Now it performs numeric addition
# # print("Sum of the two numbers:", c)
#
# # Alternatively, you can convert within the input function
# # a = int(input("Enter the first number: "))
# # b = int(input("Enter the second number: "))
# # c = a + b
# # print("Sum of the two numbers:", c)
#
# # ---- Data Types in Python ----
# # None (represents the absence of a value)
# # Numeric (int, float, complex)
# # Sequence (list, tuple, range)
# # Sets (set, frozenset)
# # Mapping (dict)
#
# # Example of Numeric Data Types
# a = 5  # Integer
# b = 5.6  # Float
# print(type(a))  # Output: <class 'int'>
# print(type(b))  # Output: <class 'float'>
#
# # Input is always treated as a string
# a = input("Enter the first number: ")
# print("Type of a is", type(a))  # Output: <class 'str'>
#
# # Conversion Example: Converting from string to integer
# a = int(input("Enter Your Weight In Kgs: "))  # Convert input to integer
# c = a * 2.1  # Converting kg to pounds (example conversion factor)
# print("Your weight in pounds is", c)
#
# # Age Calculation Example
# a = int(input("Enter Your Birth Year: "))  # Input birth year as an integer
# print("You were born in", a)
# age = 2024 - a  # Calculate age assuming the current year is 2024
# print("You are", age, "years old")
#
# # ---- String Slicing in Python ----
# # Example string
# course = "Python programming"
#
# # Slicing to extract a substring
# print(course[0:3])  # Output: 'Pyt', characters from index 0 to 2 (3 is excluded)
#
# # Accessing individual characters
# print(course[-1])  # Output: 'g', the last character (negative indexing starts from the end)
#
# # Slicing from the start to the end
# print(course[0:])  # Output: 'Python programming', entire string from index 0 to the end

# Converting integers to hexadecimal using the hex() function
print(hex(10))  # Output: '0xa', hexadecimal representation of 10
print(hex(20))  # Output: '0x14', hexadecimal representation of 20

# Assigning a hexadecimal value to a variable
k = 0xa  # '0xa' represents the hexadecimal value for 10
print(k)  # Output: 10 (converted back to decimal)

# Binary to decimal conversion
p = 0b1001  # '0b1001' represents the binary value for 9
print(int(p))  # Output: 9 (binary to decimal conversion)
