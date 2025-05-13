

# dic = {
#     "Mubeen":"human being",
#     "spoon"  : "object"
# }
# print(dic["Mubeen"])
# print(dic["spoon"])



# dic = {
#     15 : "mubeen",
#     16 : "akwa",
#     17 : "taimoor",
#     24 : "murtaza",
#     45 : "zain",
  

# }

# n = input("Enter the roll no : ")
# print(dic[int(n)])
# if (n==15,16,17,24,45):
#     print("present in class")
# else:
#     print("he is absent")    




# ##  accessing dictionary item

# info = {'Name':"Mubeen","Age":20,"Eligible":True}
# print (info)
# print(info["Name"])  # if we can want to print just one thing so we can simply put the (name,  age  ,  eligible  are other thing we can writ above)
# # so here are two method to print one thing from the  list in above if we can print our name so it can print our name if we can give him something other which is not present in list then it show error but for second method look below comment
# print(info.get("Age"))
# #  but in this method if we can give him name if it is present in the list so it show out put but if it is not present in list then it print none 



#  ########  how  access multiple value ) ###########



info = {"Name":"Mubeen","Age":20,"Eligible":True}
# print (info)
# print(info.keys())  # it will print all keys which we can taken above means that they will print the keys like(  "name", "age", "eligible") these will be print on scren
# print(info.values()) # it means when we can use this all the values can be print here like that("mubeen","20",true) 
# # if you can tskes vlue like horizontal form used like this ifyou want to print values in vertical so you can use the below method


# # # this is used to print all the answer like( "mubeen","20",true)  in line one by one
# for key in info.keys():
#     print(info[key])
# for key in info.keys():
#     print(f"the value in the coresponding key  : {key} : is :{info[key]}") # the out of this line is given below

#  ##  output  is  :  

# # (((((((( the value in the coresponding key  : Name : is :Mubeen  
# # the value in the coresponding key  : Age : is :20       
# # the value in the coresponding key  : Eligible : is :True)))))))))

   
   
   
#     # like we can tlk above how to print values in vretical lets look below

for values in info.values():
    print(info[values])    



# ##################### accessing keys################


# info = {'Name':"Mubeen","Age":20,"Eligible":True}

# print(info.items())   #  it will give keys item in pairs this like("name":"mubeen ") all keys give us in pairs 

# for key,values in info.items():
#     print(f"the value in the coresponding key  : {key} : is :{values}")