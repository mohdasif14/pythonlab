# ---- Logical Operators in Python ----

# `and` : Logical AND (both conditions must be True)
# `or` : Logical OR (either condition can be True)
# `not` : Logical NOT (negates the truth value)

# In Python, logical operators are written as:
# && -> and
# || -> or

x, y = 20, 30  # Assigning values to x and y

# Example 1: Using logical 'and'
# Both conditions must be True for the result to be True
print(x == 20 and y == 30)  # Output: True (both conditions are True)

# Example 2: Logical 'and' where one condition is False
print(x == 25 and y == 30)  # Output: False (x is not equal to 25)

# ---- Calculating the BMI of a person ----

# Formula for BMI: BMI = weight (kg) / (height (m) * height (m))

height = 1.85  # Person's height in meters
weight = 60    # Person's weight in kilograms

# Calculating BMI
bmi = weight / (height * height)  # Using the formula for BMI
print(bmi)  # Output: BMI value (approximately 17.53)

# The BMI result helps to determine if someone is underweight, normal weight, or overweight:
# - Underweight: BMI < 18.5
# - Normal weight: 18.5 ≤ BMI < 24.9
# - Overweight: 25 ≤ BMI < 29.9
# - Obesity: BMI ≥ 30
