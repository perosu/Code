import turtle
import random
def ranrun(num):
	turtle.fd(1000)
	turtle.fd(-1000)
	while num:
		a = random.randint(0,1)
		if a:
			turtle.seth(45)
			turtle.fd(5)
		else:
			turtle.seth(-45)
			turtle.fd(5)
		num = num - 1
num = input('This script used to random walk\nPlease input step number:')
ranrun(eval(num))