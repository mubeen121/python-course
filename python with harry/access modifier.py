

# three types of it:

# public modifier 
# private modifier


                                            #   public modifier

# class employes :
#     def __init__(self) :
#      self.name = "mubeen"
     
# a = employes()
# print(a.name)       #this is the public modifier  b/c w can easily access it 


                                        #  private modifier

class employes :
    def __init__(self) :
     self.__name = "mubeen"
     
a = employes()
# print(a.__name)         #this is private modifier b/c we cannot access because we can use  double underscore (  __  ) with name variable

# we cannot access it directly but there is one way to access it

print(a._employes__name)  #  here we can use access the private modifier like that so we can access it easily
# print(a.__firstlineno__) 

# print(a.__dir__())


                                    #  protected access modifier