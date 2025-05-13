
class employes : 
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def showdetail(self):
        print(f"The Name of Employee is :  { self.name} , and his ID is :  {self.id}")
        
#  AFTER  time if we want to change my clas name and we have thousand line of code so how we can change the class name so we can use inheritance for more look below

class programmer(employes):
    pass

answer = programmer("Mubeen", 400)
answer.showdetail()
# answer2 = employes("Wb", 401)
# answer2.showdetail()