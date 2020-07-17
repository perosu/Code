#2017.12.31 20:42 :version2
#A game for study.
#Guess random number.
import random
tem = input("How many times do you want to play:")
cho = int(tem)
tim = 1
while tim <= cho:
    print(tim)
    num = random.randint(1,9)
    temp = input("Guess a int number smaller than 10:\n")
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
    tim = tim + 1
print("End")

