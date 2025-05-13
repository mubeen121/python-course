 

# raising an error

a = int(input("enter value between 5 and 9 : "))
print ("hello")
if a<5 or a>9:
    raise ValueError("Enter value between 5 and 9")
#  so like this we can raise value error