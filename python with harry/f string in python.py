letter = "hey my name is {} and i am from {} "
print(letter.capitalize())
country = "Pakistan"          #   here country name can be print to his place and the second line name can be print to the name place in the above   letter   statement
name = "Mubeen khan"          #  so in print statement when we can give the line like  (  name  ) ( country  ) if wecan give country name first and name in second so it will be wrong b./c in above letter   statement we can country name can be print first and m,y name can be print second 

print(letter.format(name,country))






letter = "hey my name is {1} and i am from {0} "
print(letter.capitalize())
country = "Pakistan"       
name = "Mubeen khan"          
print(letter.format(country,name)) #( # here we can give country name first and my name one second palce if we can put   number that fisrt print it and then it so it will be print on proper position
 #lets check the program)

  #this is so difficult that give him proper position so here it has proper method which is     f string            
#in the above we can give number thast country name will print on  (  0  )  and  my name can print on (  1   )
#so here we can use   f  string  lets check below




letter = "hey my name is {} and i am from {} "
print(letter.capitalize())
country = "Pakistan"       
name = "Mubeen khan"          

print(f"hey my name is {name} and i am from {country}")  #  here we can use  f string so simply we can give name simply like



tex = "for only {price:.3f}rupees"  #   here we can use    (          price  :  .3f  )   it means that whwen number in points so you can take only three number after the point here if we can write ( .4f) so they can take four digits after the point
print (tex.format(price = 40000.99999))      




# these both are same b/c they work same b/c due this we can round off the number by three or four digits and so on


price = 40000.09999
tex = f"for only {price:.3f}rupees"
print (tex)      


print (type(f"{2*30}"))  #  when we can the f so it is string ttype if we cannot use   f    so it is int type as you can check the below   print  statement



print (type(2*30))     #   it is   int   type



letter = "hey my name is {} and i am from {} "

country = "Pakistan"       
name = "Mubeen khan"          

print(f"hey my name is {name} and i am from {country}")   # it is like this if we want that the place of {name} so the nmae cannot print just print like that statement
# so lets check the program

print (f"   hey my name is {name} and i am from {country}") # so here we can just add the  curley braces and the letter in the curley braces will not be change and it will print like as it

#  lets check it

print (f"   hey my name is {{name}}and i am from {{country}}") # so here we can just use the curley braces and it will print like as it as we can check in the print terminal













