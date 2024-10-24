# --- Recursive Function to Calculate Factorial ---
def factorial(n):
    # Base case: if n is 0, return 1 (since 0! = 1)
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Call the function with an argument of 5 and print the result
print(factorial(5))  # Output: 120
