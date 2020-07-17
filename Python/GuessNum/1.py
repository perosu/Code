#2017.12.31 20:24 :version1
#A game for study.
#Guess random number.
import random
num = random.randint(1,10)
temp = input("number:\n")
guess = int(temp)
if guess == num:
    print("Yes")
else:
    while guess != num:
        if guess <= num:
            print("Bigger")
            temp = input("Try again:")
            guess = int(temp)
        else:
            print("Smaller")
            temp = input("Try again:")
            guess = int(temp)
print("End")

