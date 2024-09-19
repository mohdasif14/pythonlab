# ---- Set Definition ----
# A set is an unordered, mutable collection of unique elements.
# Sets do not allow duplicate values, and the order of elements is not preserved (it is arbitrary).

# Creating a set with mixed data types
s = {1, 4, 5, 6, 7, "abc"}  # A set with integers and a string
print(s)  # Output may vary in order, e.g., {1, 4, 5, 6, 7, 'abc'}, sets are unordered
print(type(s))  # Output: <class 'set'>

# ---- No Repetitive Data ----
# Sets automatically eliminate duplicates
s1 = {90, 91, 90.1, 91}  # 91 appears twice, but only one instance will be kept
print(s1)  # Output: {90, 91, 90.1}, duplicates are removed

# ---- Updating a Set ----
# Adding multiple elements to a set
s1.update([88, 99])  # Adds 88 and 99 to the set
print(s1)  # The position of elements is random due to the unordered nature of sets

# ---- Removing Elements from a Set ----
# Removing an element from the set
s1.remove(88)  # Removes 88 from the set
print(s1)  # Output: 88 is now removed


s1.remove(88)

# ---- Frozen Set ----
# Creating a frozen set (an immutable version of a set)
f = frozenset(s1)  # Once frozen, the set cannot be modified (no add, remove operations allowed)
# print(f)  # Output: frozenset({90, 91, 90.1, 99})

#create a list of countries start first with 3 countries in a list then add a country to the list then remove a country
# from the list at any specif index then add a country in the middle of the list

# Creating a list of 3 countries
countries = ["India", "USA", "Germany"]
print(countries)  # Output: ['India', 'USA', 'Germany']

# Adding a country to the list
countries.append("Australia")  # Adding "Australia" to the end of the list
print(countries)  # Output: ['India', 'USA', 'Germany', 'Australia']

# Removing a country from a specific index (removing "USA" at index 1)
del countries[1]
print(countries)  # Output: ['India', 'Germany', 'Australia']

# Adding a country in the middle of the list (insert "Canada" at index 1)
countries.insert(1, "Canada")
print(countries)  # Output: ['India', 'Canada', 'Germany', 'Australia']
