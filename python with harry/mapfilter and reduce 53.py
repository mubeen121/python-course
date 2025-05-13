# def  new_fun(x):
#     return x*x*x

# print(new_fun(3))



# l = [2,3,4,5,6]
# # #if we want to find the cube of all the number in aray we can use this method

# newl = []
# # # for item in list1:
# # #     newl.append(new_fun(item))        but to use of this method we can simply use map method

# newl = list(map(new_fun,l))
    
# print(newl)



# l = [2,3,4,5,6]
# def filter1(a):      # in this method we can use filter method which means that ever condition we can give here if it satisfy show that element or return fale
    
#     return a>8

# newlist = list(filter(filter1,l))
# print(newlist)





# reduce method 



from functools import reduce


number = [1,2,3,4,5]

def mysum(x,y):
    return x+y

sum = reduce(mysum,number)

print(sum)
