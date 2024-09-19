# Create a list of countries; start first with three countries in a list, then add a country to the list; remove a
# country from the list at specific index and then add a country in the middle of the list as well do same process
# with a set as well.

#List
countries_list = ['India', 'USA', 'Germany']
countries_list.append('Canada')
print("After adding a country:", countries_list)

countries_list.pop(1)
print("After removing the second country:", countries_list)

countries_list.insert(1, 'Japan')
print("After inserting a country in the middle:", countries_list)

#Set
countries_set = {'India', 'USA', 'Germany'}
countries_set.add('Canada')
print("After adding a country:", countries_set)

countries_set.remove('USA')
print("After removing a country:", countries_set)

countries_set.add('Japan')
print("After adding a country:", countries_set)