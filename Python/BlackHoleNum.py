in1 = eval(input("This script is used to black hole number.\nPlease input a number:"))
print("\n")
past = 1000
tof = 1
while tof:
    num = list([in1//100,in1%100//10,in1%10])
    num.sort()
    buffer = (num[2]*100 + num[1]*10 + num[0]) - (num[0]*100 + num[1]*10 + num[2])
    if past == buffer:
        print("\nThe black hole number is %d.\nThis number use %d times."%(buffer,tof-1))
        tof = 0
    else:
        past = buffer
        in1 = buffer
        print("Time %d: "%tof+str(buffer))
        tof = tof +1
