# Taking an integer input from the user and converting it to an integer type
a = int(input("Enter any number: "))

# Indentation in Python is very important. It means adding spaces or tabs before a block of code.
# In this case, the code inside the 'if' and 'else' statements must be indented, showing they are part of those blocks.

# Checking if the number is even
if a % 2 == 0:  # If 'a' divided by 2 has a remainder of 0, the number is even
    # The following line is indented to indicate it's part of the 'if' block
    print("a is even")  # This will be executed if the condition above is true

# Else block will execute when the number is odd (not divisible by 2)
else:
    # The following line is indented to indicate it's part of the 'else' block
    print("a is odd")  # This will be executed if the 'if' condition is false
