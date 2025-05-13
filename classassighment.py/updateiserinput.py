
my_array = [15, 25, 35, 45, 55]
def update_array(arr, index, new_val):
    if 0 <= index < len(arr):
        arr[index] = new_val
        return True  
    else:
        return False  
print(f"Current array: {my_array}")
try:
    index_to_update = int(input("Enter the index to update (0 to {}): ".format(len(my_array) - 1)))
    new_value = int(input("Enter the new value: "))
except ValueError:
    print("Invalid input. Please enter valid integers for the index and value.")
    exit()
if update_array(my_array, index_to_update, new_value):
    print(f"Updated array: {my_array}")
else:
    print("Index is out of bounds. Update failed.")