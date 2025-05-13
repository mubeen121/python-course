
     
countries = ("spain", "india" ,"pakistan", "itlay","england")
temp = list(countries) # here we can convert   tuple   into list the we can add and remove something
temp.append  ("russia")  #  add one name
temp.pop(3)              # remove the name on the following index
countries = tuple(temp) #  here we can change  list   again to     tuple    b/c what change we want in a tuple so we can made that changes and convert the list again to tuple
print (countries)




#################################(               how we can merge two tuple      )###########################

countries = ("spain", "india" ,"pakistan", "itlay","england")
countries2 = ("srilanka", "london","america")

newtuple = countries + countries2
print(newtuple)


#######################(     tuple method                 )##########################################

                
             ##############(         count tuple    )########################

tuple1 = (0,1,2,3,2,3,1,3,2)
#  so here we can give new name and then we can count it
t1 = tuple1.count(2)
print("Two can come("   ,t1,    ")time in the tuple")


       ############################(  index in tuple         ) ##################################


tuple1 = (0,1,2,31,2,3,1,3,2)

t1 = tuple1.index(31)    #  here we can find the index of the value that which index the number have
print("Two can come in index  = "   ,t1,    )




tuple1 = (0,1,2,31,2,3,1,3,2)

t1 = tuple1.index(3,4,8)   # here we can said that value (  3  ) can   find  from   index (   4   )  to  index  (  8   ) so here they can show the index of first preference  means that which index they will come first so that index  number will be print on  screen
print("the search  number can come on index  = "   ,t1,    )




###################################(      how to find length of tuple       ###############################


tuple1 = (0,1,2,31,2,3,1,3,2)
p = len(tuple1)
print(p)



