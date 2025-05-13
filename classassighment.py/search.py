
my_array = [11, 20, 35, 49, 55, 60, 70, 80, 90]


element_to_search = 55


def search_array(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
  
result = search_array(my_array, element_to_search)

if result :
    print(f"Element:  {element_to_search}  :  found at index    {result}.")
else:
    print(f"Element {element_to_search} not found in the array.")