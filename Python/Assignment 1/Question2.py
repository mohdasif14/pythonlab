# Question 2
# Create a tuple of six elements of different types

my_tuple = ('Hello', 42, 3.14, True, [1, 2, 3], {'key': 'value'})

print("First element:", my_tuple[0])
print("Third element:", my_tuple[2])

print("Length of the tuple:", len(my_tuple))

element_to_check = 42
if element_to_check in my_tuple:
    print(f"The element {element_to_check} exists in the tuple.")
else:
    print(f"The element {element_to_check} does not exist in the tuple.")