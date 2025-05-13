
my_array = [1, 2, 3, 4, 5]
def search_array(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  
    return -1 
print(f"Current array: {my_array}")
try:
    element_to_search = int(input("Enter the element to search: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for the element.")
    exit()
result = search_array(my_array, element_to_search)

if result != -1:
    print(f"Element {element_to_search} found at index {result}.")
else:
    print(f"Element {element_to_search} not found in the array.")