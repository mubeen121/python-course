
my_array = [10, 20, 30, 40, 502]
def delete_array(arr, position):
    if 0 <= position < len(arr):
        del arr[position]
        return True 
    else:
        return False 
print(f"Current array: {my_array}")
try:
    position_to_delete = int(input("Enter the position to delete (0 to {}): ".format(len(my_array) - 1)))
except ValueError:
    print("Invalid input. Please enter a valid integer for the position.")
    exit()
if delete_array(my_array, position_to_delete):
    print(f"Updated array: {my_array}")
else:
    print("Position is out of bounds. Deletion failed.")