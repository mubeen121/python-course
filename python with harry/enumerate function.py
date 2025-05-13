
marks = [12,35,67,98,1,55,88]

# index = 0
# for mark in marks :
#     print(mark)
#     if index==3:
#         print("Mubeen khan")
#     index = index+1   # if we want to make this code easier so we can write it like that


for index,mark in enumerate(marks,start=1):  # but if we want to print my name before on that index so we can simply write  (  start = 1  ) which means that you can print the name before that index
    print(mark)
    if index==3:
        print("mubeen khan")