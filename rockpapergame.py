import random
computer=random.choice([-1,0,1])
youstr=input("enter your choise :")
youDict={"r": 1,"p": -1,"s": 0}
revesedict={1: "rock" , -1: "paper" , 0: "scissor"}
you=youDict[youstr]
print(f"enter your choise : {reversedict[you]}/n computers choise : r{reversedict[computer]}")
if(computer==you):
    print("match draw")
else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("you loose")
    elif(computer==1 and you==-1):
        print("you loose")
    elif(computer==1 and you==0):
        print("you win ")
    elif(computer==0 and you==1):
        print("you loose")
    elif(computer==0 and you==-1):
        print("you win")
    else:
        print("somthing went wrong")