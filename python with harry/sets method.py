s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))  #so here we can take  union (union means to cme two sets ) so we can combine two sets (s1)    (s2) 
# so due to it both sets are combine and make one sets

# if we want to just print the sets not combine it so lets check it
print(s1,s2)


####################(    update  function   )########################


s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
# here we can use update function lets check it

s1.update(s2) # here we can want to update the list   (  s1  )  and take the value from   (   s2  ) which is not present in   (  s1   )
#in this the set is update with union if we can know unoin so we know what function perform in update place



# ###########################(    intersetion    )#################

p1 = {1,2,5,6}
p2 = {3,6,7,5,2}
print(p1.intersection(p2))  #  intersetion is used to take common from both the sets
p1.intersection_update(p2)
print (p1)



 ###############################( symmetric difference)#################################



p1 = {1,2,5,6}
p2 = {3,6,7,5,2}
print(p1.symmetric_difference(p2))   # this function is used to to show us that which element is not equal to both sets

p1.symmetric_difference_update(p2)
print (p1)


########################(difference and difference update )################################


p1 = {1,2,5,6}
p2 = {3,6,7,5,2}
print(p1.difference(p2))    #  in this w can simply says that only print those number which is present in   (set A)  but not present in  (set  B)

p1.difference_update(p2)
print (p1)



# ################(       isdisjoint       )#########################


p1 = {1,23,53,63}
p2 = {3,6,7,5,2}
print(p1.isdisjoint(p2)) #  in this it will show false if one number is present in both sets and  it will show true when both sets are different from each other means that no number can match in both sets



########################(     issubset      )##################################


p1 = {1,2,3,4}
p2 = {1,2,3,4}
print(p1.issubset(p2))   # it wil show when all number are same in both set so it will show true if one number is different so it will show false


# ######################## (      issuperset        )##################################


p1 = {1,2,3,4,4,5}
p2 = {1,2,3,4,5,6}
print(p1.issubset(p2))  # this also same as subset b/c inthis we can check that if values  in  p2  is fulley present in  p1 so it show true or if there is one ore two value cannot be match so it also show true 
# or we can says that subset  is opposite to  superset

############################(   add method    )######################################


# if we can add something in sets 

p1 = {1,2,3,4}
p1.add(1000000)
print(p1)



############################(   update method    )######################################


p1 = {1,2,3,4}
p2 = {5,6,7,8,9}
p1.update(p2) #  it simply means that add sets(p2) element in set(p1) and primt it on screen
print(p1)




# ############################(    remove/discard  method   )############################


# just remove one element from the sets

p1 = {1,2,3,4}
p1.remove(1)
print(p1)

 ###   discard method 

# same as remove method but just one difference is that that if some thing is not present in list and we can use remove method then it show error if we can use discard then it cannot show error

p1 = {1,2,3,4}
p1.discard(1)
print(p1)



###################################(   pop method   )#######################################




p1 = {1,2,3,4}
item = p1.pop()  # if we wnat to remove any one number so we can use pop when we can use it  it can pop one value by its own 
print(p1)         #  but it can be pop any one number it is not fixed
print (item)


# #############################(    del  method   )#####################################

# p1 = {1,2,3,4}
# del p1             # it show error because all the value can be remove from the sets
# print(p1)


##################################(  clear method     )#################################


p1 = {1,2,3,4}
p1 .clear() # this is the method if we can clear our set means that all element can be remove from the sets but the set cannot be delete so we can use clear method when we can use clear method and then print the set then it can show empty set b/c we can just remove element not entire set
print(p1)


# #####################( check if item is exist )#############################


info = {"Mubeen",2,3,5,6,7,8,True}
if "Mubeen" in info:
    print("Yes (Mubeen)  is present in the set")
else:
    print("Mubeen is not present")    