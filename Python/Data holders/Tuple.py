# ---- Tuple Definition ----
# A tuple is an ordered, immutable (cannot be changed) collection of items.
# Unlike lists, tuples are fixed once defined and cannot be modified (no addition, deletion, or updating).

# Creating a tuple with a single element
tpl = (20)  # This is just an integer, not a tuple, because there's no trailing comma.
# To create a single-element tuple, we must add a comma after the value: tpl = (20,)

# Creating a tuple with multiple elements
tpl2 = (20, 23, 20, 45, 67, "super")  # A tuple with mixed data types: integers and a string

# Accessing tuple elements and performing operations

# Printing the second tuple
print(tpl2)  # Output: (20, 23, 20, 45, 67, 'super')

# Counting occurrences of an element in the tuple
print(tpl2.count(23))  # Output: 1, because the number 23 appears only once in the tuple

# Finding the index of the first occurrence of an element
print(tpl2.index(23))  # Output: 1, because 23 is found at index 1 (second position)

# Slicing the tuple to access a range of elements
print(tpl2[0:2])  # Output: (20, 23), slicing from index 0 to 2 (exclusive of index 2)

# Getting the length of the tuple
print(len(tpl2))  # Output: 6, as the tuple has 6 elements

# ---- List to Tuple and Tuple to List Conversions ----

# Converting a list to a tuple
lst = [1, 2, 3, 4, 5]  # A simple list with integers
print(type(lst))  # Output: <class 'list'>, showing that 'lst' is a list

# Converting the list to a tuple
tpl3 = tuple(lst)  # Using the tuple() function to convert 'lst' into a tuple
# print(tpl3)  # Output: (1, 2, 3, 4, 5), now 'tpl3' is a tuple

# Converting the tuple back to a list
lst2 = list(tpl3)  # Using the list() function to convert 'tpl3' back to a list
# print(lst2)  # Output: [1, 2, 3, 4, 5], now 'lst2' is a list again
