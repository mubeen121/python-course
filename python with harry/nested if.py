num= int(input("ENTER THE NUMBER :  "))
print("ENTER NUMBER IS  :", num)
if(num<0):
    print("first condition is correct")
elif(num>=0):
    if(num<=10):
        print("It's correct print this statement")
    elif( num<=60):
        print("OTHERWISE THIS STATEMENT I Print CORRECT IF ABOVE IS INCORRECT")
    else:
        print("No one is match")
else:
    print("if all are false then at last this statement will print")


