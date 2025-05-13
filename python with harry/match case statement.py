# x= 10
# match x :
#     case 0 :
#         print("X is zero")
#     case 4 :
#         print("X is four")
#     case _ :
#         print("not match") # this is first step we can simply match the value

        # now we can take value from user
        # lets check it
               
x=int(input("Enter the value : "))
print("The value is : " , x ," : lets check the match case ")
match x :
    case 0 :
        print("X is zero")
    case 4 :
        print("X is four")
    case _ if x==40 :
        print(x,"is equal to 40")
    case _ if x<=60 :
        print(x," yes it is less than or it's  60")

    case _ :
       print("not match")


        