# --- Example 1: Function with return statement ---

# Define a function 'avg' to calculate the average of two numbers
def avg(a, b):
    return (a + b) / 2  # Return the result of (a+b)/2 to the caller

# Call the avg function with arguments 10 and 20 and print the result
print(avg(10, 20))  # Output: 15.0

# --- Example 2: Function without return statement ---

# Define a function 'average' that prints the average of two numbers directly
def average(a, b):
    print("The average of the two numbers is", (a + b) / 2)  # Print the result

# Call the average function with arguments 20 and 30
average(20, 30)  # Output: The average of the two numbers is 25.0

# --- Example 3: Function that performs multiple operations and returns multiple values ---

# Define a function 'calculator' that performs addition, subtraction, multiplication, and division
def calculator(a, b):
    w = a + b  # Addition
    x = a - b  # Subtraction
    y = a * b  # Multiplication
    z = a / b  # Division

    return w, x, y, z  # Return all four results as a tuple

# Call the calculator function with arguments 10 and 20 and store the result
result = calculator(10, 20)

# Print the result, which is a tuple containing the four operations
print(result)  # Output: (30, -10, 200, 0.5)
