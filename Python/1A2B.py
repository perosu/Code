#2018.3.4 15:49
#Author:ArchG
#A simple 1A2B game
#Version 1
import random

list1 = [str(random.randint(0,9)),str(random.randint(0,9)),\
str(random.randint(0,9)),str(random.randint(0,9))]
#print (list1) TestCode

print ("Please input 4 number,you have 5 times")
cou = 5
                
while cou:
    print("-------------------------------------------------")
    print("Round",6-cou)
    a = input("Num1:\n")
    b = input("Num2:\n")
    c = input("Num3:\n")
    d = input("Num4:\n")
    A = 0
    B = 0
    if a ==list1[0]:
        A = A+1
    elif a ==list1[1]:
        B = B+1
    else:
        if a ==list1[2]:
            B = B+1
        else:
            if a == list1[3]:
                B = B+1
    if b ==list1[1]:
        A = A+1
    elif a ==list1[0]:
        B = B+1
    else:
        if a ==list1[2]:
            B = B+1
        else:
            if a == list1[3]:
                B = B+1
    if c ==list1[2]:
        A = A+1
    elif a ==list1[0]:
        B = B+1
    else:
        if a ==list1[2]:
            B = B+1
        else:
            if a == list1[3]:
                B = B+1
    if d ==list1[3]:
        A = A+1
    elif a ==list1[1]:
        B = B+1
    else:
        if a ==list1[2]:
            B = B+1
        else:
            if a == list1[0]:
                B = B+1
    if d ==list1[0]:
        A = A+1
    elif a ==list1[1]:
        B = B+1
    else:
        if a ==list1[2]:
            B = B+1
        else:
            if a == list1[3]:
                B = B+1
    if A == 4:
        print("You win!")
        print("-------------------------------------------------")
        cou = 0
    else:
        print (A,"A",B,"B")
        cou = cou-1
