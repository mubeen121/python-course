
# class person:
#     name = "Mubeen"
#     occupation = "game developer"
#     age = 20

# # a = person()   # here we can assigh the class name into the variable to make it easy to remember 


# # here we can create a class and add some information in it about a person and thwn print it 

# # but if i want to chnage name or age or occupation so we can simply do it

# person.name = "khan"
# person.age = 21
# person.occupation = "Developer"
# print(person.name ,  person.occupation,person.age)

#  like that we can change everything in the class



class person:
    name = "Mubeen"
    occupation = "game developer"
    age = 20
    def info(self):           # here we can creat a function and assign him somthing and in parameter we can givte the (  self  ) keyword so it can call the other variable itself we can just simply define it
        print(f"{self.name} is a {self.occupation}")

a = person()
a.name = "zain"
a.occupation = "sad boy"
a.info()

b = person()
b.name = "hassan"
b.occupation = "farig"
b.info()

c = person()
c.name = "afzal"
c.occupation = "dollars trader"
c.info()



# here we can create alot of othervariable and assign him the value of the class and we cannot create a class again and again