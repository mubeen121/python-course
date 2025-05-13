#  in last video we can create a class and give him some value and then w can change the value and also creat new variable and give him different values  
#  so now we can use the constructor to make it more easy 

# class person:
#     name = "Mubeen"
#     occupation = "game developer"
#     age = 20
#     def info(self):          
#         print(f"{self.name} is a {self.occupation}")
# a = person()
# a.info()

#  first we can create a class like this now we can use the constructor


class person : 
    def __init__(self,name,occ):          # here we can use the (  __init__  ) keyword and give him some argument to pass from it and and can only declare that argument and in second function we can pass it and when we can call a function the argument we can give in the function we can give him value when we call it so it can work so like that we can give alot of value and print him on screen 
        self.name = name            
        self.occ = occ                         
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a = person("Mubeen" , "developer")
b = person( "WB" , "HR")
a.info()
b.info()