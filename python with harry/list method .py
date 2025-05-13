l = [1,2,3,4,5]
print(l)

#  but if we can use (   append    ) method it means add one thing more
# lets check it

l.append(7)
l.append("mubeen")  # so mubeen   and    7    can   be add into the list due to    append mathod

print (l)

    ####################(                 sort method                 )##################################
    
    

#when we can use this method so if we can give value in array in mix order so they will sort it like ascending and decending #


number = [9,8,7,6,5,4,3,2,1]
print (number)
number.sort()  
print(number)




  ###### ##################  (        reverse    method for sort ()           ###################################)


l1 = [5,4,3,2]
print (l1)
l1.sort()
print(l1)
l1.sort(reverse = True)
print (l1)



########(                               reverse  method          )######################

list = [1,2,3,4,5,6,7,8,9]
print(list)
list.reverse()  #  if we can use this method so they can print all the values in reverse form like (1,20,13,40,50) so these can be print like that  (  50,40,13,20,1) 
#  so let we can do it in program
print (list)


              ############(        index method                  )################################


list = [1,2,3,4,5,6,7,8,9]
print (list)
print(list . index(4))  #   so due to index method we can find that the following number is present on the following index
 #lets check this in program

##############################(               count method              )#################################


list = [1,2,3,4,5,6,7,8,9,3,3,3]
print (list)
print(list. count(3))  #  in this method we can count the digit it means that the following digit come in the array how many time    
print (list)         



###########################(                 copy method               )####################################

list = [1,2,3,4,5,6,7,8,9,3,3,3]
print (list)
m = list.copy()  # if we can use this method so the following array can be copy and can be print as well b/c we can used copy method
print(m)

# but this method is different from that b/c we can put    m[0]=0     so when the array print so at zeero index zero can be print
#   if we can put any number there    m[0] =  0   if we can change index location and assign him any  value so  that value can be print on that index

m=list
m[0 ]= 0
print(list)



#############################(            insert method          )#####################################



list = [1,2,3,4,5,6,7,8,9,3,3,3]
print (list)
#  how to insert value in the list 
# so lets check the program 

list.insert(1,300)#  here we can said taht we can put   value  (  300  )  at the index  ( 1 )
list.insert(5,800)
# so lets check is its working or not 
print(list)




#       #######################(        extend method           )#################################



# this is the method that we can merge two list
l= [1,2,3,4,5,6,7,8,9] 
print (l)
m = [300,400,200,500]
l.extend (m)  #  here we can said that taht the new list (  name (m))  can be put at the end of the old list(  nmae  (l)) 
# lets check is it working
print(l)


     # ############         #(another method of merge a list)      ################                    #####################

l= [1,2,3,4,5,6,7,8,9]
print (l)
m = [300,400,200,500]
# so here we can simply write 
k = l+m
print (k)









l = [11, 45, 1, 2, 4, 6, 1, 1]

print(l)
l.append(7)
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(1))
m = l.copy()
m[0] = 0
l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
print(k)
l.extend(m)
print(l)
l.clear()

lists = [1,2,3,4,5]
lists1 = len(lists)
print(lists1)
