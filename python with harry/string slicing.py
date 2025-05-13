name= "mubeen , khan"
print (name [0:6])#it means that if you want to print that name but you don't want to print fill name so you can write 
                  #that variable which you can assign a name and in print statemnt and give him command to print namumber to only that point 


# IF WE WANT TO FIND THE LENGTH OF THE STRING                  
name = "mubeen,khan"
print(len(name))



fruit= "mango"
mangolen=len(fruit)# here we can declare with another name   mangolen     and then print it so the will give him the length of mango
print(mangolen)
# but if we want to print just print first two are three letter of mango so the print statememnt are as follow:
print(fruit[0:4])# so just print    mang     not full name b/c we cannot give him full cmmand we can say him to print only four character
#   but if we want to skip first letter and print remanining letter so print srtatememnt are as follow:
print (fruit[1:5])
# if we cannot give zero at start like this ( 0:4   )  (:4)  so python have this ability that hey put (  0  )  by itself and show us result let check it work or not
print(fruit[:4])#   let check result in terminal


#  anther trick of it are if we write print statememnt like this   PRINT(FRUIT[:])     SO THEY WILL print full b/c they can check the condtion and show us result let gets check it#
print(fruit[:])  #let check result in terminal

# so slicing are work like that


#  IF WE CAN TALK ABOUT NEGATIVE SLICING LET CHECK BELOW

fruit= "mango"
# print (fruit[0:-3])  ## it means that you can minus  3   from the length of mango and it frint just two words  (mango length is   5   and we can  minus  3 so  remaninig is  2)

#another negative slicing like this below
print(fruit[-1:-3])# lets check what will be print here
# so there is nothing be print here b/c this not make any sense so nothing will be print 
#but if can change places of    (- 1)  and (-3)  then we can check the  result
 
 #   let check it

print(fruit[-3:-1]) # what will be print here

# here can print     (   ng   )  how it print it concept are given below
 
 # it means that( -3+5=2)  and    (-1+5=4)  so here can print   (2) index   and  (4)  index   value  son in index     2    are  n     and index  4   are    g   

alphabet="abcd"
for l in alphabet:               # for loop printing
      print(l)
      











