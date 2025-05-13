# in this method of import we can just import the module and then written math again and again when we can perform any math function

# import math
# result = math.floor(4.3424)
# print(result)


#  and from here we can use from which means that in math module we can use these methods only so we can write from and then import math and written function name which we can perform

#
# from math import sqrt,pi
# result = sqrt(9)*pi
# print(result)
#
#
# #  and here we can import math with from and then use sterick ( * ) so all the method inside the math will import here, and we cannot write math again, and again we can just write method name
# #  But we cannot use it b/c here all function are import into the code and here will make confusion so we can write the function name which we want from math module
#
#
# from math import *
# result1 = sqrt(10)
# print(result1)
#
#
# from math import sqrt as s
# result2 = s(10)
# print(result2)
# #  what is mean of it :  ais ka matlab ha ka ham sqrt ku short name sa donate kar lataa ha pir program ma ( sqrt ) ki jaga ham sirf  ( s ) bi lik saktaa ha
#
#
# # dir function
#
# import math
# print (dir(math))  # if we want to print all the function in math module so we can the ( dir ) function so it can print all the function in math module


# here we can import our created module with name mubeen.py so let check

# from mubeen import welcome, mubeen1

# welcome()
# print(mubeen1)

#  so here we can successfully import our defined module into another file using import method

# import math
# result = math.sqrt(9)
# print(result)

# import math as m 
# sum  = m.floor(4.939)
# print(sum)

# from math import ceil as c 
# new = c(4.888)
# print(new)

# from math import pi
# one = pi
# print(one)

# from math import *
# new_1 = sqrt(6)*pi
# print(new_1)

# import math
# print(dir(math))

# import pandas
# print(dir(pandas))

from mubeen import welcome , mubeen1
welcome()
print(mubeen1)