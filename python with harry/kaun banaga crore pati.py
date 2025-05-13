
questions =[
            ["which language was used to create fb?",
            "python","french" ,"javascript","php","none",4],

             ["which language was used to create fb?",
            "python","french" ,"javascript","php","none",4],

             ["which language was used to create fb?",
            "python","french" ,"javascript","php","none",4],

             ["which language was used to create fb?",
            "python","french" ,"javascript","php","none",4],

            ["which language was used to create fb?",
            "python","french" ,"javascript","php","none",4],

            ["which language was used to create fb?",
            "python","french" ,"javascript","php","none",4],

            ["which language was used to create fb?",
            "python","french" ,"javascript","php","none",4],

             ["which language was used to create fb?",
            "python","french" ,"javascript","php","none",4],
            ]
levels = [1000,3000,6000,7000,8000,10000,20000,32000]
money = 0
for i in range(0,len(questions)):
    question = questions [i]
    print (f"question for Rs. {levels[i]}")
    print(f"a.{question[1]}          b.{question[2]}")
    print(f"a.{question[3]}          b.{question[4]}")
    reply = int(input("enter your answer (1-4) or 0 to quit :"))
    if reply==0:
        money=levels[i-1]
        break
    if reply==question[-1]:
        print(f"correct answer,you have won Rs.,{levels[i]}")
        if (i==0):
            money = 10000
        elif(i==7):
            money = 32000
    else:
        print("wrong answer ! ")
        break

print(f"Congrulation you won {money} total")

