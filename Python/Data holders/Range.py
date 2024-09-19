#The range() function in Python generates a sequence of numbers.
# It is commonly used in loops when you need to iterate
# over a series of numbers. The range() function can take one,
# two, or three arguments:


# Creating a range of numbers from 0 to 4
r = range(5)  # This will generate numbers from 0 to 4 (range(5) means 0, 1, 2, 3, 4)
print(r)  # Output: range(0, 5), this is a range object

# Iterating over the range using a for loop
for i in r:
    print(i)  # Output: 0, 1, 2, 3, 4 (numbers generated by the range)

# Creating a range from 2 to 5 (inclusive of 2, exclusive of 6)
r2 = range(2, 6)  # This will generate numbers 2, 3, 4, 5
print(r2)  # Output: range(2, 6)

# Iterating over the second range
for i in r2:
    print(i)  # Output: 2, 3, 4, 5

# Creating a range from 2 to 5 with a step of 3 (skipping numbers in between)
r3 = range(2, 9, 3)  # This will generate numbers starting at 2, with a step of 3: 2, 5, 8
print(r3)  # Output: range(2, 9, 3)

# Iterating over the third range
for i in r3:
    print(i)  # Output: 2, 5, 8

    # for i in r:
    #     print(i)  # This print statement should be indented under the for loop
