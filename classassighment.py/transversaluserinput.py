
try:
    num_elements = int(input("Enter the number of elements in the array: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for the number of elements.")
    exit()
my_array = []
for i in range(num_elements):
    try:
        element = int(input(f"Enter element {i + 1}: "))
    except ValueError:
        print(f"Invalid input. Please enter a valid integer for element {i + 1}.")
        exit()
    my_array.append(element)
def traverse_array(arr):
    for element in arr:
        print(element, end=" ") 
    print()  
print("Array elements:")
traverse_array(my_array)