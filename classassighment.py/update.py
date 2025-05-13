
my_array = [10, 25, 34, 40, 55,80,90]
index_to_update = 5 
new_value = 100  
def update_array(arr, index, new_val):
    if 0 <= index < len(arr):
        arr[index] = new_val
        return True  
    else:
        return False
if update_array(my_array, index_to_update, new_value):
    print(f"Updated array: {my_array}")
else:
    print("update failed you are going out of loop")