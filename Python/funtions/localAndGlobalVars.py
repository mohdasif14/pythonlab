# Global variable 'a'
a = 10  # This variable is declared in the global scope and can be accessed anywhere outside functions.


# --- Function Example with Local Variables ---
def display():
    y = 20  # Local variable inside the function
    a = 90  # Local variable 'a', it shadows the global 'a' inside this function
    print(a, y)  # Prints local 'a' and 'y', output will be "90 20"


# Print global 'a' (not affected by the local 'a' in the function)
print(a)  # Output: 10 (global 'a' is used outside the function)


# --- Function to display a name with a greeting ---
def displayname(name):
    print("hello " + name)  # Concatenates "hello " with the passed name


# Call the function with the argument "Asif"
displayname("Asif")  # Output: "hello Asif"


# --- Function with a Nested Function Example ---
def displayname2(name):
    # Inner function that returns a greeting
    def message():
        return "Hello "

    # Concatenate the result of 'message()' with the provided name
    result = message() + name
    return result  # Return the final result


# Call the function and print the result
print(displayname2("Asif"))  # Output: "Hello Asif"


# --- Function to Iterate and Print List Elements ---
def fun(lst):
    for i in lst:  # Loop through each element in the list 'lst'
        print(i)  # Print the current element


# Call the function with a list as argument
fun([1, 2, 3, 4, 5])  # Output: prints each number in the list on a new line
