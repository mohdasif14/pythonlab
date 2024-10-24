# Binary to hexadecimal conversion
d = 0b1010  # '0b' indicates a binary literal (in this case, 10 in decimal)
q = hex(d)  # Converts the binary number to a hexadecimal string
# print(q)  # Output: '0xa' (the hexadecimal representation of 10)

# Boolean expressions: Used to compare values, returning True or False
# print(9 < 8)  # Output: False, because 9 is greater than 8

# Another comparison using variables
a = 10  # Assigning 10 to the variable 'a'
b = 100  # Assigning 100 to the variable 'b'
# print(b < a)  # Output: False, because 100 is not less than 10

# ---- Dynamic Data Storage Types in Python ----
# 1. List: Mutable (changeable) sequence of items. Items can be of mixed data types.
# 2. Tuple: Immutable (unchangeable) sequence of items.
# 3. Set: Unordered collection of unique items (no duplicates allowed).
# 4. Range: Represents a sequence of numbers, commonly used in loops.
# 5. Dictionary: A collection of key-value pairs, where each key is unique.
# 6. Bytes: Immutable sequence of bytes, used for binary data.

# ---- Working with Lists ----
lst = [5, 6, 7, 8, 9, "xyz"]  # List that contains both integers and a string

# print(lst)  # Output: [5, 6, 7, 8, 9, 'xyz'], displaying the list

# Creating an empty list
lst1 = []  # An empty list
# print(lst1)  # Output: [], an empty list with no elements

# Checking the length of the list
# print(len(lst))  # The len() function returns the number of elements in the list (output: 6)

# Repeating the list multiple times
# print(lst * 5)  # Output: Repeats the list 5 times, concatenating it repeatedly

# Modifying a list element by index
lst[1] = 16  # Changing the second element (index 1) from 6 to 16
# print(lst)  # Output: [5, 16, 7, 8, 9, 'xyz']

# Appending a new element to the end of the list
lst.append(100)  # Adds 100 at the end of the list
# print(lst)  # Output: [5, 16, 7, 8, 9, 'xyz', 100]

# Removing an element from the list
lst.remove(100)  # Removes the element 100 from the list
# print(lst)  # Output: [5, 16, 7, 8, 9, 'xyz']

# Inserting an element at a specific position
lst.insert(2, 5)  # Inserts the value 5 at index 2 (third position)
# print(lst)  # Output: [5, 16, 5, 7, 8, 9, 'xyz']

# Deleting an element by its index
del lst[0]  # Deletes the first element (index 0)
# print(lst)  # Output: [16, 5, 7, 8, 9, 'xyz']

# ---- Working with Another List (Numerical Operations) ----
lst2 = [10, -10, 800, 5]  # A list of integers, including negative numbers

# Finding the maximum value in the list
# print(max(lst2))  # The max() function returns the largest value in the list (output: 800)

# Finding the minimum value in the list
# print(min(lst2))  # The min() function returns the smallest value in the list (output: -10)

# Sorting the list in ascending order
lst.sort()  # Sorts the list in place (ascending order)
# print(lst)  # Output: [5, 7, 8, 9, 'xyz'] (Sorting does not work if list has mixed types like int and str)

# Sorting the list in descending order
lst.sort(reverse=True)  # Sorts the list in descending order
# print(lst)  # Output: [9, 8, 7, 5], if the list contains comparable elements

# Clearing all elements from lst2
lst2.clear()  # Removes all elements from the list
# print(lst2)  # Output: [], the list is now empty
