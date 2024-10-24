# Print numbers starting from 50 up to 70, with a step of 2
for x in range(50, 71, 2):  # range(start, stop, step)
    print(x)

lst = [2, 3, 4, 5, 6, 7]

product = 1  # Initializing the product to 1
for x in lst:
    product *= x  # Multiply product by the current element in the list
    print(product)  # Print the intermediate product after each multiplication

print(product)  # This will print the final product

# Use of break to stop loop execution
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
for x in lst2:
    if x == 6:  # When x equals 6, break the loop
        break
    print(x)  # Print values until the loop encounters 6

# Use of continue to skip certain values
# Printing numbers from 1 to 20, but skipping multiples of 3
for x in range(1, 21):  # Loop from 1 to 20
    if x % 3 == 0:  # If x is divisible by 3, skip this iteration
        continue
    print(x)  # Print x if it's not a multiple of 3
