
#    in this we can see how we can pass argument  lets get started



# def average (a = 4,b = 5):                       # if we can give value to  a  and b   so it's average will be shown but if we can give the value in below like in average paranthesis so they will ignore the value of the a and b and give average of the value which we can put in averrage paranthesis
#     #lets check 
#     print("the average is ", (a+b)/2)
# average(a=4,b=6)  




 # in this  thwy will show the average of (  4,6  ) not the value of ( a, b)
# if we can give only the value of  (  a  ) so it can take the value of  (    b   ) automatically by the above average value
  
   # four types of argument in which we can provide by function

   # (1) defult argument
   # (2) keyword argument
   # (3) variable length argument
   # (4) required argument

    # in the above case (   a  ,  b ) are required argument


    ########################(               keyword augment      )###############
    
    # in this argument it is not required to give   a    first   if you can   give   b   value first and then then it will show no error

     #lets check the example



# def keyword(a,b):
#     print ("the total is",(a+b)*2)
# keyword( b=4,a=2)




#   #    here we can give three, four, five, and ten   value also   #    lets check the program
# def keyword(a,b,c):
#     print ("the total is",(a+b+c)*2)
# keyword( b=4,a=2,c=2)




#####################(                variable length argument        )###########################


def average (*number):                  # there is imp to put (   *   ) of taking the is tuple
    print(type(number))# we can check it's type                   # this number is taken as a tuple (  what is tuple we can search about it)
    sum = 0
    for i in number:
        sum = sum + i
    print ("The average is", sum/len(number))     #  this line means that the sum of  the number ( average(5,6,4)) ( 5+6+4 ) is divide by it's length so the length is    (  3  ) b/c  5,6,4 are three so this is it's length and 
average(5,6,4)



  # if i can take my argument as a dictionary  ( dict )

def name (**name):
    print(type(name))
    print("Hello , ", name["fname"] , "My name", name["mname"], name["lname"])
name(mname = "Mubeen",lname = "Khan",fname = "khan bahadur")


 
 #              ##############(      return statement    )###################



def average (*number):               
  
    sum = 0
    for i in number:
   
        sum = sum + i
                          # print ("The average is", sum/len(number)) 
    
    return sum/len(number)  # here we can want to return the value of this number (sum/len(number)) if we can want to return something other from this vlaue so we can write that value in the   front   of return what we want
 
#  here if we want to use return they will give the same value like the above print statement
c = average(5,6,4,1,2)
print("The return value is  = " ,c)
















 
  
   
    
     














