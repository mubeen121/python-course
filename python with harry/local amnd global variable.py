# x= 4
# print(x)

# # here we can say that ( x ) is a global variable b/c it can work inside the function and also work outside the function

# def hello():
#     x = 5  # and this ( x ) is a local variable b/c it can work only inside the function we cannot print it outside the function so this is called local variable
#     y = 2
#     print("hello i am mubeen")
#     print(f"this is local variabl{x}")
# hello()

# # print(y)    here if we want to print ( y ) outside the function so it can showw error b/c they can say that y is not defined so that why it can show error b/c it can inside the function

# print(f"it is global variable{x}")

#  if we want to print the value of  ( x )  outside the function which define inside the function so it cannot print b/c it can take global variable

#   but if we want to print the value of ( x ) which define inside the function so we can simply do that

def new_func():
    global x
    x=5
    print("hello")
    
new_func()
print(x)  # so here we can simply write global x and the value of x inside the function can print outside the function