
 ###############################( update method)##############################



classonemarks = {12: 49, 14:56, 16:80} # here we can say taht we have roll number like (  12, 14 16) and his marks is (49, 56,80)
# here we can store marks of diffeent student in a variable
anothersectionmarks = {13:66 , 15:77 , 20:33}# lets suppose we have another marks of another section 

#  so when result time we can come result of both the classes 
#then

classonemarks.update(anothersectionmarks) #  so due to this we can combine marks of both the classes

print (classonemarks)  # so due this both class can be combine to one 
# set is unordered  whike due this new python version dictionary is ordered

#
###########################(   clear method )################################


classonemarks = {12: 49, 14:56, 16:80} 
anothersectionmarks = {13:66 , 15:77 , 20:33} 

print (classonemarks)
 
 #  if we can want to clear the whole dicttonary so we can use clear method 
 # lets check below

#  lets we can clear the   whole dictionary 

classonemarks.clear()
print(classonemarks)  # so in result they can show us empty dictionary b/c we can clear the dictionary



 
 ########## ###############(  pop method  )#####################################



classonemarks = {12: 49, 14:56, 16:80} 


classonemarks.pop(14) # here if we can want to pop the value so due to this method the value can be pop/remove
print (classonemarks) # so here ( 14 ) can be pop/ remove



 ######################(  pop item  )##################################

#  this method can simply remove the last pair in dictionary



classonemarks = {12: 49, 14:56, 16:80} 

classonemarks.popitem()  #  so here it can just remove the last item if we can put some value then it show error b/c   (  pop item ) cannot required any argument/value

print (classonemarks)





# #####################(   del function  )#####################################


classonemarks = {12: 49, 14:56, 16:80} 


del classonemarks[16] 
 # if we cannot write something here so it can delete all the dictionary #   or if we can give that del this thing so they can delete it  it is also same like  ( pop, remove)

print (classonemarks)