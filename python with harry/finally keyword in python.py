

 # the code in finally keyword can be excute if there is error in program or not

# ################(  finally clause)###############


def func1():

    try:
        l = [1,2,3,4,5]
        i = int(input("enter the index : "))
        print(l[i])
        return True # if i can put every thiing here so it can be execute lets suppose if i can write here(    i    ) so the value of i can be execute
    except:
         print("Some error occured in program")
         return False
    finally:
        print("I am always execute")  # when we can put this method ( finally  ) so this can be execute if this program is true or false it can be print in every condition
# we can say that when if ir is return then no more can be excute but this finally can can be execute in every condition
x = func1()
print(x)






















