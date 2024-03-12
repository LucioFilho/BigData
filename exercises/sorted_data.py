'''The list of tuples is created by zipping together two lists: 
inventory_names and inventory_numbers. Here's the code transcribed 
from the image:'''

# Given lists
inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 23, 43]

# Combine the lists into a list of tuples
combined_list = list(zip(inventory_names, inventory_numbers))

# 1. Sort this list by inventory numbers
sorted_comp_num = sorted(combined_list, key=lambda inv_tuple: inv_tuple[1])

# 2. Sort this list by length of the inventory name
sorted_comp_name = sorted(combined_list, key=lambda inv_tuple: len(inv_tuple[0]))

# Print the sorted list by name length
print(sorted_comp_name)

'''This code will output the combined_list sorted by the length of the inventory names. 
If you also want to see the list sorted by inventory numbers, you can add a print 
statement for sorted_comp_num:'''

# Print the sorted list by inventory numbers
print(sorted_comp_num)

'''The lambda functions are used as the key for the sorted() function to specify 
how the items should be compared during the sort. The first lambda function sorts 
the tuples by the second item (inventory numbers), and the second lambda function 
sorts them by the length of the first item (the names of the inventory items).'''