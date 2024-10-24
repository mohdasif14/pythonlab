# Getting item names from user input and converting them to lowercase
item1_name = input("Enter the name of the first item: ").lower()
item2_name = input("Enter the name of the second item: ").lower()
item3_name = input("Enter the name of the third item: ").lower()
item4_name = input("Enter the name of the fourth item: ").lower()
item5_name = input("Enter the name of the fifth item: ").lower()

# Getting item quantities, ensuring they are integers
item1_quantity = int(input(f"Enter the quantity of {item1_name}: "))
item2_quantity = int(input(f"Enter the quantity of {item2_name}: "))
item3_quantity = int(input(f"Enter the quantity of {item3_name}: "))
item4_quantity = int(input(f"Enter the quantity of {item4_name}: "))
item5_quantity = int(input(f"Enter the quantity of {item5_name}: "))


# Creating a dictionary to store item prices
prices = {
    "apple": 10,
    "banana": 10,
    "milk": 25,
    "bread": 5,
    "egg": 8,
    # Add more items and their prices here if needed
}


# Getting the prices of the entered items from the dictionary
item1_price = prices.get(item1_name, 0)  # Default price is 0 if the item isn't found
item2_price = prices.get(item2_name, 0)
item3_price = prices.get(item3_name, 0)
item4_price = prices.get(item4_name, 0)
item5_price = prices.get(item5_name, 0)



# Calculating the total cost for each item
total_cost_item1 = item1_quantity * item1_price
total_cost_item2 = item2_quantity * item2_price
total_cost_item3 = item3_quantity * item3_price
total_cost_item4 = item4_quantity * item4_price
total_cost_item5 = item5_quantity * item5_price


# Calculating the grand total
sub_total = total_cost_item1 + total_cost_item2 + total_cost_item3 + total_cost_item4 + total_cost_item5
tax = sub_total*0.18
grand_total = sub_total+tax


# Displaying the results
print("\n--- Receipt ---")
print(f"{item1_name.capitalize()}: Quantity = {item1_quantity}, Unit Price = ₹{item1_price}, Total Cost = ₹{total_cost_item1}")
print(f"{item2_name.capitalize()}: Quantity = {item2_quantity}, Unit Price = ₹{item2_price}, Total Cost = ₹{total_cost_item2}")
print(f"{item3_name.capitalize()}: Quantity = {item3_quantity}, Unit Price = ₹{item3_price}, Total Cost = ₹{total_cost_item3}")
print(f"{item4_name.capitalize()}: Quantity = {item4_quantity}, Unit Price = ₹{item4_price}, Total Cost = ₹{total_cost_item4}")
print(f"{item5_name.capitalize()}: Quantity = {item5_quantity}, Unit Price = ₹{item5_price}, Total Cost = ₹{total_cost_item5}")
print(f"\nGrand Total: ₹{grand_total}")
