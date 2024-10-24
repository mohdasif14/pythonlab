# A dictionary is an unordered, mutable collection of key-value pairs.
# In Python, dictionaries are defined by placing items inside curly braces {},
# with each item consisting of a key and its associated value, separated by a colon :.

# ---- Creating a Dictionary ----

# Example of creating a dictionary using curly braces
my_dict = {
    "name": "Alice",   # Key: "name", Value: "Alice"
    "age": 25,         # Key: "age", Value: 25 (integer)
    "city": "New York" # Key: "city", Value: "New York"
}

# Example of creating a dictionary using the dict() function
my_dict2 = dict(name="Bob", age=30, city="Los Angeles")

# ---- Accessing Values ----

# Accessing values using the key with square brackets
print(my_dict["name"])  # Output: Alice, retrieves the value associated with the key "name"

# Accessing values using the get() method
print(my_dict.get("age"))  # Output: 25, retrieves the value associated with the key "age"
print(my_dict.get("country", "Not Found"))  # Output: Not Found, key "country" does not exist, returns default value

# ---- Adding and Updating Key-Value Pairs ----

# Adding a new key-value pair
my_dict["country"] = "USA"  # Adds a new key "country" with the value "USA"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}

# Updating an existing key-value pair
my_dict["age"] = 26  # Updates the value of the key "age" to 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}

# ---- Removing Key-Value Pairs ----

# Removing a key-value pair using the del statement
del my_dict["city"]  # Removes the key "city" and its associated value
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'country': 'USA'}

# Removing a key-value pair using the pop() method
age = my_dict.pop("age")  # Removes the key "age" and returns its value
print(age)  # Output: 26
print(my_dict)  # Output: {'name': 'Alice', 'country': 'USA'}

# ---- Dictionary Methods ----

# Keys of the dictionary
keys = my_dict.keys()  # Returns a view object of all keys
print(keys)  # Output: dict_keys(['name', 'country'])

# Values of the dictionary
values = my_dict.values()  # Returns a view object of all values
print(values)  # Output: dict_values(['Alice', 'USA'])

# Items (key-value pairs) of the dictionary
items = my_dict.items()  # Returns a view object of all key-value pairs
print(items)  # Output: dict_items([('name', 'Alice'), ('country', 'USA')])

# Copying the dictionary
copy_dict = my_dict.copy()  # Creates a shallow copy of the dictionary
print(copy_dict)  # Output: {'name': 'Alice', 'country': 'USA'}

# Clearing the dictionary
my_dict.clear()  # Removes all key-value pairs
print(my_dict)  # Output: {}

# ---- Nested Dictionaries ----

# Creating a nested dictionary (dictionary inside a dictionary)
nested_dict = {
    "person": {
        "name": "John",
        "age": 30
    },
    "location": {
        "city": "Boston",
        "state": "MA"
    }
}

# Accessing values in a nested dictionary
print(nested_dict["person"]["name"])  # Output: John
print(nested_dict["location"]["city"])  # Output: Boston
