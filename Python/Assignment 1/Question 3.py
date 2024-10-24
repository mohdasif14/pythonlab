
# Create a string
my_string = " You are Awesome "

sliced_string = my_string[4:7]  # Slicing "are"
print("Sliced string:", sliced_string)

lstrip_string = my_string.lstrip()
rstrip_string = my_string.rstrip()
strip_string = my_string.strip()
print("Left stripped:", lstrip_string)
print("Right stripped:", rstrip_string)
print("Fully stripped:", strip_string)


find_result = my_string.find("Awesome")
print("Find 'Awesome':", find_result)


count_result = my_string.count("e")  # Counts occurrences of 'e'
print("Count of 'e':", count_result)


remove_result = my_string.replace("Awesome", "")
print("After removing 'Awesome':", remove_result)