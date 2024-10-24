# Printing numbers from 1 to 20
i = 1
while i <= 20:
    print(i)
    i += 1  # Increment by 1

# Printing odd numbers from 1 to 20
a = 1
while a <= 20:
    print(a)
    a += 2  # Increment by 2 to ensure 'a' remains odd



# Define lower bound (LB) and upper bound (UB)
LB = 2  # Minimum number
UB = 30  # Maximum number

# Initialize x as the lower bound
x = LB

# Check if x is even; if so, make it the next odd number
if x % 2 != 0:
    while x <= UB:
     print(x)  # Print the current odd number
     x += 2  # Increment by 2 to get the next odd number

