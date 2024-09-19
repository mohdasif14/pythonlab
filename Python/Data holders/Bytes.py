# Creating a list with integers and a string
lst = [1, 2, 3, "asif"]  # A list with both integers and a string

# Checking the type of the list
print(type(lst))  # Output: <class 'list'>, confirming it's a list

# Converting the list to a bytes object
# This will throw an error because "asif" is a string and bytes can only handle integers between 0 and 255
b = bytes(lst)
print(type(b))  # This will not run because of the error in the line above

# Each element of the list for a bytes object should be an integer less than 255

# Example of creating a list that can be converted to a bytes object (uncomment to test):
# lst = [1, 2, 3]  # All elements are integers and less than 255
# b = bytes(lst)  # Successfully converts the list to bytes
# print(type(b))  # Output: <class 'bytes'>

# Converting the list to a bytearray object
# This will also raise an error due to the presence of a string in the list
b1 = bytearray(lst)  # bytearray expects all elements to be integers between 0 and 255
print(type(b1))  # This will not run because of the error in the line above

# Correct list for bytearray (uncomment to test):
# lst = [1, 2, 3]  # A list of integers
# b1 = bytearray(lst)  # Converts the list to a mutable bytearray object
# print(type(b1))  # Output: <class 'bytearray'>


#corrected version
lst = [1, 2, 3]  # All elements are integers less than 255

# Converting to bytes
b = bytes(lst)
print(type(b))  # Output: <class 'bytes'>

# Converting to bytearray
b1 = bytearray(lst)
print(type(b1))  # Output: <class 'bytearray'>
