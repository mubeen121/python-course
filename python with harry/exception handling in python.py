

#  # if we want that our program cannot show error so we can do this method we cannot say that they cannot show error but if there is error inn first line then they can print the   (   except case     )

# a = input("Enter the number : ")
# print(f"Multiplication table of {a} is : ")
# try:
#           for i in range(1,11):
#                     print(f"{a} x {i} = {int(a)*i}") 
#                                                      #  her we can make the  table of if we can put any number so the table of this number is printed 
# except  :
#   print(  "invalid input !")  # when  there is an error in program so simply this line can be excute
  
# print ("some imp line of code")
# print ("end of program ")
  
     
     

# #  other method of printed of the same line######


# a = input("Enter the number : ")
# print(f"Multiplication table of {a} is : ")
# try:
#           for i in range(1,11):
#                     print(f"{a} x {i} = {int(a)*i}") 
# except Exception as e :
#   print(e) # if we can write  ( e ) here so the problem of error can be printed if we can write something other here so that line can be printed lets check we can print (  e  ) in the below print statement
#   print(  "invalid ") # if we can write  ( e ) here so the problem of error can be printed if we can write something other here so that line can be printed lets check we can print (  e  ) in the below print statement
  
# print ("some imp line of code")
# print ("end of program ")
  
  
  
  
  
  
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num]) # here if we can enter wrong index number so it can show index error   or   if we can enter some invalid string so it can show (value error)
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")














