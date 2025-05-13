
##recurion is just like function   in a function we can make another function so this is called recursion

#what is factorial  =  it means from that number you can come downward and multiple
 #example:
            #if we can take  factorial of 5 so it become = factorial of 5 is (  5*4*3*2*1  ) so this is the factorial of  (5)
# factorial(5) = (5*4*3*2*1)
# factorial(4) = (4*3*2*1)
# factorial(3) = (3*2*1)
# factorial(2) = (2*1)
# factorial(1) = (1)
# factorial(0) = (1)
 # factorial (0) is equal to  (  1   )
 #so like this we can take factorial

# factorial(n) = n * factorial (n-1)  #this the formula


def factorial(n):
    if n==0 or n==1:
      return 1
    else:
       return n*factorial(n-1)

print (factorial(5))
# print (factorial(4))
# print (factorial(3))
# print (factorial(2))          # so this is the method to find factorial
# print (factorial(1))
# print (factorial(0))



#   #    fibonacci sequence


# f1 = 0
# f2=   1
# f3 = f1+f2
# f4 = f2+f3
# f5 = f3+f4
# f6 = f4+f5
# f7 = f5+f6
# f8 = f6+f7
# f9 = f7+f8
# f10 = f8+f9
# print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10)

def fibanocci(n):
   if (n==0 or n==1):
      return 1
   else:
      return fibanocci(n-1)+fibanocci(n-2)
   
print(fibanocci(5))




# def factorial(n):
#   if(n==0 or n==1):
#     return 1
#   else:
#   # fact = factorial(4)
#     return n*factorial(n-1)
  
# print(factorial(0))














