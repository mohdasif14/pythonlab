# # Assigning values to variables
# a, b = 20, 3  # Assigning 20 to 'a' and 3 to 'b'
# print(a, b)  # Prints: 20 3
#
# # Using 'sep' (separator) to customize how values are separated
# print(a, b, sep=',')  # Output: 20,3
# print(a, b, sep='++++')  # Output: 20++++3

# Assigning values to more variables
name = "Asif"
marks = 98.5

# Using the print statement with placeholders/data specifiers

# %s is used for strings, %f for floating-point numbers
# print('Name is %s, marks are %f' % (name, marks))  # Output: Name is Asif, marks are 98.500000

# Explanation:
# %s - String placeholder (used for the 'name' variable)
# %f - Floating-point placeholder (used for the 'marks' variable)

# You can format the floating point number to limit decimal places:
# print('Name is %s, marks are %.2f' % (name, marks))  # Output: Name is Asif, marks are 98.50


# Using the .format() method to insert variables into the string
# '{}' acts as a placeholder, and the variables are inserted in order
print('Name is {}, Marks are {}'.format(name, marks))  # Output: Name is Asif, Marks are 98.5

# Using numbered placeholders
# {0} corresponds to the first variable 'name', and {1} corresponds to the 'marks' variable
print('Name is {0}, Marks are {1}'.format(name, marks))  # Output: Name is Asif, Marks are 98.5

# Assigning a new variable
grade = 'A'

# Printing multiple values using a simple comma-separated method
print('Name is', name, 'Marks are', marks, 'Grade is', grade)  # Output: Name is Asif Marks are 98.5 Grade is A

# Using the .format() method with multiple placeholders, including an additional variable
# Here, {0} is replaced by 'name', {1} by 'marks', and {2} by 'grade'
print('Name is {0}, Marks are {1}, Grade is {2}'.format(name, marks, grade))  # Output: Name is Asif, Marks are 98.5, Grade is A
