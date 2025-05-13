
   ##################(        list           )#########################


l = [1,2,3,4,56,7,8,9,10]

print (l)
print ("The type of l is = ",type(l))
print(l [0])
print(l [4])

#if there are come another data type in the list  like string or bolean 

     # answer  yes   another data type can be exist in one list 

l = [1,2,3,4,56,7,8,9,10,"mubeen",True,""]   # bolean have may be true or may be false

print (l)
print ("The type of l is = ",type(l))
print (l[9])
print (l[10])

  ##############################(negative indexing  )######################################

#  negative indexing are as follow

list = [12,42,30,"Mubeen",True]   # bolean have may be true or may be false
print (list)


#   these all are print same value b/c when you can check the condition of all it has same meaning 
#  lets check whatever it is treu what i said or false

print (list[-3])      #  NEGATIVE INDEX B/C IT WILL COUNT THE LIST from back side
print (list[5-3])  #positive index
print(list[len(list)-3]) # positive index
print(list[2])  #  positive index


 #  check whatever an item present in the list?
 
 #lets check

if 7 in list:
    print ("yes")
else :                         #  when we can check an item in the list so we can do this 
    print ("No")    

if "een" in "mubeen":
    print ("Yes")
else:
    print ("No")



list = [12,42,30,"Mubeen",True]  
print (list)
print (list[3:5])   # if we can give here any number so it will be starrt from this and end from that 
#   lets check

print(list [1:3])   # here we can give him taht only print from (   1   to    3) on screen so they can print just that from screen  

list = [12,42,30,"Mubeen",True]  
print (list)
print (list [1:-1])  #   so here they have in neagtive index so we can convert it to positive index
#  it means taht make it positive like this  (      1   :    4    )so  (  -1)index and   (4)  index are equal b/c if we can take it from (-) so they start from the back 
#   # lets check the problem

print (list [1:-1])
print (list[1:4])  #   they both will give the same out put


   #######(      jumping    index     )###############



list = [12,42,30,"Mubeen",40,50,10,35,55,33,77] 
print (list)

# so here we can use the jumping 

print (list[1:11:4])  #  so here can  jump from two index b/c we can give him (  2  ) so they can jump with (  2  )index
#  lets check it









marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print(marks[-3]) # Negative index
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index

if "6" in marks:
  print("Yes")
else:
  print("No")

# Same thing applies for strings as well!
if "Ha" in "Harry":
  print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)



















