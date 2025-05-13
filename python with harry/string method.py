
                        ###### (  STRINGS ARE IMMUTIABLE)##########


a = "mubeen"
print(len(a)) # this is simple print the number that how many letter are they have
 
 # but if we can put     
                             #########   (   UPPER CASE  ) #########     

 #   in it so thwe name can print in in caplita letter let see it

print (a.upper())  # so let check check the result the name can print in capital

# AND NEXT   IS     
#                            ######### (     LOWER CASE     )   ####### 
#LETS CHECK

print(a.lower())   #  so can check resullt all the letter are print in small letter


                                   # ########## (   RSTRIP     )###########

a= "Mubeen!!!!!!!!!!!!"
print(a.strip("!"))   # it means that this sign cannot be shown with my name 
 
 # let check the result in terminal

 # but there is one problem if we can put exclamatory mark and then write a name so they cannot remove the sign
 
 #lert check the result in terminal

a="!!! mubeen !!!!!"
print(a.rstrip("!"))  # lets check the result


                            #########    (       REPLACE     )#############

a="mubeen"
print(a.replace("mubeen","Mubeen khan"))  # this can replace your the name with the3 second name which we can give in print statement

#  lets check the result  in terminal


#                      #################  (   SPLIT METHOD  )###############
#     FOR EXAMPLE 
a = "Mubeen  khan !!!!!!!!!!"

# so the above  name  (Mubeen  khan  !!!!!!!!)     can be written in list form mean they all are print in screen in list
#lets check the program

print(a.split(" "))   # you must give the space in double codes in print statement

# check the terminal

                       # ####### (         CAPITALIZE  METHOD      )############

a= "introduction to python"
# so you see that the first letter of the    introduction is small so tyhis method is used to make the first letter capital

print(a.capitalize())

# if you can write any other word capital which is small so  (   capiltlize     )   can make it correct
#  let check the example if can write  a sentence mix of capital  and small letter so it can be correct by this method
# 
# # LETS CHECK THE PROGRAM 

a = "introDUctiON  tO  pYTHON"

#  lets check it will be correct using this method

print(a.capitalize())

# so check the terminal it will work




                      # #######  (        CENTER() METHOD      )    ########

a=" WELOCOME TO PYTHON"    
#   When we can use this method so they can take the sentence in the mid of the page
#  lets check the program
                  
print(a.center(150))  #   the (    150     )   is the vlue which show that the sentence are print where 
#  it's also work great


# lets if we can check the length if it so lets check it

print(len(a))  # it show ( 19 ) when you count it it length will be ( 19 ) as we can study in before topics

#  the new thing is that if can check the length of the     (center method)  so it show us the result that how much value we can give in center method

print(len(a.center(150)))  # so it show us (  150 ) b/c we can give center value ( 150 ) so it show that length



     #          #################(        COUNT METHOD        )###############

a= " mubeen mubeen mubeen "
# this methodtells us that how much time the name come in the sentence
#let's check it

print(a.count("mubeen")) 

# it show output (  3  ) so you can check that i will give the name three time so it wil show it three time

#                       ##########(     ENDSWITH METHOD       )##############

#   this method tells that is this method end with the last value lets check
a= "mubeen khan"

#lets check if this method end with (   khan     )

print (a.endswith("khan"))
#check result it show   (true)   it means that it ends with khan


# another method  in this that what index number we can write in print statement can ends with it or not]
#lets check
a="Welcome to the Console !!!"
print(a.endswith("to",4,10))


#    ################(    find method     )############
a="My name is mubeen khan"
# if we can find something in it so the below method will be used
print(a.find("an"))
# so it show (  20  )b/c   (   an   ) is on index 20

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))  # but in this sentence (  is   ) is used two time so it show the (   is    )which come first
# if the value not match with the vlau we can find then it show (    -1    )


#             ##########################(       index method      )###########


#The index() method searches for the first occurrence of the
#  given value and returns the index where it is present.If given value is absent from the string then raise an exception.


a= "mubebn khan"
print(a.index("bn"))

#if the value is present it will print otherwise it will show error


#                                      #######(    isalnum method     )############

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False

a="hello how are you"

print(a.isalnum())  ## it will show false b/c we can used all are small if we can used first letter of every word and remaining alphabet are small so it show  and not give any space so it show    true  
#if we can give space with the words so it show false  
#### so check both the program the above and the below the above show false and below show true
###next thing not 
# lets check it
b="HelloHowAreYou"
print(b.isalnum())

##  ###############(    isalpha    )############

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

a= "welcome"
print(a.isalpha()) # it show true when all the word are samll  or   all the word are capital or all the words are integer then it show true 
# 
#lets check
a="Welcome00"
print(a.isalpha())
# it will show false b/c there are some integer and some are alphabet

##### ##################(          islower       )#########################

#The islower() method returns True if all the characters in the string are lower case, else it returns False.

a="Mubeen"
print(a.islower()) #it will show error b/c there are first letter are capital and remaninig are small  but in this case all the alphabet are small then it show true

str1 = "hello world"
print(str1.islower())

#    ##########    (      isprintable method  )###############

a=" we can wish you eid mubarak"
print(a.isprintable()) #it will show us true b/c all the word are printable if we can put backslash it show false b/c backlash are not printable means t just command not a string or integer


#   ##########(      isspace       )#############

mk= "   "
print(mk.isspace())  #  it show true only if there are white space if there is no space it not show true it show false

#   ################(     istitle method    )#############

# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
#  lets check
a="Mubeen"
print(a.istitle())

# it show false when first letter is small

#   #############    (     isupper     )#############

# The isupper() method returns True if all the characters in the string are upper case, else it returns False
# it means all the letter must be true
a="MUBEEN"
print(a.isupper())


#       ###############(      startswith method      )#################

# it is like endswith  in this method that if this sentence start with this word

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))#  check result it show true b/c it star with python



#  #############(        swapcase       )####################

# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) #in this capital convert to small and small letter convert to capital


#   #################(           TITLE METHOD     )########################


# The title() method capitalizes each letter of the word within the string.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title()) # they can convert first letter of every word in the sentence into capital