import random
i=1
list=["st","pa","sc"]
user=0
pc=0
while(i<=10):
    n=input("enter any one of these 'st' for stone 'pa' for paper 'sc' for scissor : ")
    computer=random.choice(list)
    if n=="st" and computer=="pa":
        print("pc")
        pc=pc+1
        i=i+1
        continue
    elif n=="st" and computer=="sc":
        print("user")
        user=user+1
        i=i+1
        continue
    elif n=="pa" and computer=="st":
        print("user")
        user=user+1
        i=i+1
        continue
    elif n=="pa" and computer=="sc":
        print("pc")
        pc=pc+1
        i=i+1
        continue
    elif n=="sc" and computer=="st":
        print("pc")
        pc=pc+1
        i=i+1
        continue
    elif n=="sc" and computer=="pa":
        print("user")
        user=user+1
        i=i+1
        continue
    elif n==computer:
        print("tie")
        i=i+1
        continue
print("GAME\nOVER")
print("user ",user, "pc ",pc)