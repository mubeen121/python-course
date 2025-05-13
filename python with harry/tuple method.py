
#                ###########(            tuple              )#####################


#  when we can use tuple so we can use this bracket   ()
# but if we can use list it will represent by this bracket  []


# it is like list but here is one difference  :::
#  list can be changed   but tuple cannot be changed
# this is the main difference b/w ( list  and  tuple)

#here other tdata type value wioll be exit but when we can made a tuple so we cannot be change it



# tu = (1) # if we can write like this so it show the   (  int  class )  b/c it is just a integer
# print (type())
# t = (1,) # it will show the   (  class   tuple  ) b/c we can put comma here
# print(type())

tup = (1,2,3,5,6,342,234,456,45,213)
print (len(tup))
print(tup)
print(type(tup))
print (tup[0])
print (tup[1])
print (tup[2])
print (tup[3])
# print (tup[30])  # so this will show error b/c we have not index of this value


# if we  can check some number in the tup
#so it will be check like this

if 6 in tup:
    print("welcome")
else:
    print ("Not welcome")    

tup2=tup[3:8]   #  here we can form new tuple and give him command to take the number from this index to this index and form new tuple
 ##  here we can also perform slicing
print(tup2)







tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  34 in tup:
  print("Yes 342 is present in this tuple")
else:
  print("Number are not present")
tup2 = tup[1:4]
print(tup2)



                    # (                   concatenation method in tuple                 )


newtup = (1,2,3,4,5)
print(newtup)
tuple2 = (6,7,8,9,0)
newone = newtup+tuple2
print(newone)



#  if we want todo  something in tuple we can first make it list then do whatever we want  then print the new tuple

tup1 = (1,2,3,4,5,5,1,1,1)
tup2 = tup1.count(1)
print(tup2)