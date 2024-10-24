# # Taking user input for a name
# s = input("Enter Your Name: ")  # 's' will store the name as a string
#
# # Taking user input for a number (will be stored as a string)
# i = input("Enter a Number: ")  # 'i' will be a string
#
# # Converting the input directly to an integer
# i2 = int(input("Enter a Number: "))  # 'i2' will be an integer because of the int() conversion

# Taking multiple numbers separated by commas and converting them into a list of integers
# Using the split(',') method to separate values by commas
# Taking user input for three numbers separated by commas
lst = [x for x in input("Enter three numbers separated by commas: ").split(',')]  # Splits input by commas and stores them in a list
# Taking user input for three numbers separated by commas
lst2 = [int(x) for x in input("Enter three numbers separated by commas: ").split(',')]


# Displaying the list
print(lst)
