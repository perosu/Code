#2019.4.27
#ArchGu
import random as rd
import curses
import numpy as np
import os
stdscr = curses.initscr()

class game:
    def __init__(self):
        self.canvas = np.zeros([4,4])
        self.temp = []
        self.tempnum = None
        self.rannum = None
        self.key = None
        self.bool1 = 1
        self.bool2 = 1
    def add(self):
        for x in range(4):
            for y in range(4):
                if self.canvas[x,y] == 0:
                    self.temp.append([x,y])
        self.tempnum = len(self.temp)
        self.rannum = rd.randint(0,self.tempnum-1)
        self.canvas[self.temp[self.rannum][0],self.temp[self.rannum][1]] = 2
    def show(self):
        os.system("clear")
        for y in range(4):
            print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b%d\t%d\t%d\t%d\t" % (int(self.canvas[0,y]),int(self.canvas[1,y]),int(self.canvas[2,y]),int(self.canvas[3,y])))
        print("\n")
    def com(self):
        self.key = stdscr.getch()
        if (self.key == ord('w')):
            while self.bool1 | self.bool2 :
                self.bool1 = 0
                self.bool2 = 0
                for y in range(2,-1,-1):
                    for x in range(4):
                        if (self.canvas[x,y]) == 0 & (self.canvas[x,y+1] != 0):
                            self.canvas[x,y] = self.canvas[x,y+1]
                            self.canvas[x,y+1] = 0
                for y in range(2,-1,-1):
                    for x in range(4):
                        if (self.canvas[x,y] == 0) & (self.canvas[x,y+1] != 0):
                            self.bool1 = 1
                for y in range(2,-1,-1):
                    for x in range(4):
                        if (self.canvas[x,y] != 0) & (self.canvas[x,y+1] == self.canvas[x,y]):
                            self.canvas[x,y] = self.canvas[x,y] * 2
                            self.canvas[x,y+1] = 0
                for y in range(2,-1,-1):
                    for x in range(4):
                        if (self.canvas[x,y] != 0) & (self.canvas[x,y+1] == self.canvas[x,y]):
                            self.bool2 = 1
        elif (self.key == ord('s')):
            for y in range(1,4,1):
                for x in range(4):
                        if (self.canvas[x,y] == 0) & (self.canvas[x,y-1] != 0):
                            self.canvas[x,y] = self.canvas[x,y-1]
                            self.canvas[x,y-1] = 0
                for y in range(1,4,1):
                    for x in range(4):
                        if (self.canvas[x,y] == 0) & (self.canvas[x,y-1] != 0):
                            self.bool1 = 1
                for y in range(1,4,1):
                    for x in range(4):
                        if (self.canvas[x,y] != 0)& (self.canvas[x,y-1] == self.canvas[x,y]):
                            self.canvas[x,y] = self.canvas[x,y] * 2
                            self.canvas[x,y-1] = 0
                for y in range(1,4,1):
                    for x in range(4):
                        if (self.canvas[x,y] != 0) & (self.canvas[x,y-1] == self.canvas[x,y]):
                            self.bool2 = 1
        elif (self.key == ord('a')):
                for x in range(2,-1,-1):
                    for y in range(4):
                        if (self.canvas[x,y] == 0) & (self.canvas[x+1,y] != 0):
                            self.canvas[x,y] = self.canvas[x+1,y]
                            self.canvas[x+1,y] = 0
                for x in range(2,-1,-1):
                    for y in range(4):
                        if (self.canvas[x,y] == 0) & (self.canvas[x+1,y] != 0):
                            self.bool1 = 1
                for x in range(2,-1,-1):
                    for y in range(4):
                        if (self.canvas[x,y] != 0) & (self.canvas[x+1,y] == self.canvas[x,y]):
                            self.canvas[x,y] = self.canvas[x,y] * 2
                            self.canvas[x+1,y] = 0
                for x in range(2,-1,-1):
                    for y in range(4):
                        if (self.canvas[x,y] != 0) & (self.canvas[x+1,y] == self.canvas[x,y]):
                            self.bool2 = 1
        elif (self.key == ord('d')):
            for x in range(1,4,1):
                for y in range(4):
                        if (self.canvas[x,y] == 0) & (self.canvas[x-1,y] != 0):
                            self.canvas[x,y] = self.canvas[x-1,y]
                            self.canvas[x-1,y] = 0
                for x in range(1,4,1):
                    for y in range(4):
                        if (self.canvas[x,y] == 0) & (self.canvas[x-1,y] != 0):
                            self.bool1 = 1
                for x in range(1,4,1):
                    for y in range(4):
                        if (self.canvas[x,y] != 0) & (self.canvas[x-1,y] == self.canvas[x,y]):
                            self.canvas[x,y] = self.canvas[x,y] * 2
                            self.canvas[x-1,y] = 0
                for x in range(1,4,1):
                    for y in range(4):
                        if (self.canvas[x,y] != 0) & (self.canvas[x-1,y] == self.canvas[x,y]):
                            self.bool2 = 1
        elif (self.key == ord('q')):
            exit()
x = game()
while True:
    x.com()
    x.add()
    x.show()
