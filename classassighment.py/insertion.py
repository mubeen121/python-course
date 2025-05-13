# Initialize an array
my_array = [1, 2, 3, 4, 5]

# Element to be inserted
element_to_insert = 6
element_to_delete = 2 

# Position at which to insert the element (0-based index)
insert_position = 2

# Insert the element at the specified position
my_array.insert(insert_position, element_to_insert)
my_array.remove(element_to_delete)

# Print the updated array
print(my_array)