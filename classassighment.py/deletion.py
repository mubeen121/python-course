# Initialize an array
my_array = [1, 2, 3, 4, 5]

# Element to be deleted
element_to_delete = 3

# Check if the element is in the array
if element_to_delete in my_array:
    # Remove the first occurrence of the element
    my_array.remove(element_to_delete)
else:
    print(f"{element_to_delete} not found in the array")

# Print the updated array
print(my_array)