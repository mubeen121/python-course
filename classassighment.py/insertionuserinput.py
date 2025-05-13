
my_array = [1, 2, 3, 4, 5]
def insert_array(arr, position, value):
    if 0 <= position <= len(arr):
        arr.insert(position, value)
        return True  
    else:
        return False  
print(f"Current array: {my_array}")
try:
    position_to_insert = int(input("Enter the position to insert (0 to {}): ".format(len(my_array))))
    new_value = int(input("Enter the new value to insert: "))
except ValueError:
    print("Invalid input. Please enter valid integers for the position and value.")
    exit()
if insert_array(my_array, position_to_insert, new_value):
    print(f"Updated array: {my_array}")
else:
    print("Position is out of bounds. Insertion failed.")