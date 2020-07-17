class caesar:
    def __init__(self,input1):
        self.input1 = input1
        self.dict1 = [[15,3,0],[3,0],[18,3,0,9],[20, 5, 6, 0, 5],[4, 0],[16, 18, 0, 0, 2, 16, 16]]
        #code dict to ensure the original word
        self.dict2 = [101,102,101,99,107,99]
        #code dict to ensure the number of ascii code
        print(self.input1)#test code
    def encode(self,word):
        self.word = word
        self.num = []
        self.code = []
        self.lenth = len(self.word)
        for i in range(self.lenth):
            self.num.append(ord(self.word[i]))
        minum = sorted(self.num)
        for j in self.num:
            self.code.append(j-minum[0])
        self.dict1.append(self.code)# append the code to dict
        self.dict2.append(minum[0])#append the code to dict
        print(self.code)
        print(minum[0])
    def turnw(self,word,change):
        self.word = word
        self.change = change
        self.turned = []
        self.lenth = len(self.word)
        for i in range(self.lenth):
            if (ord(self.word[i]) + change <= 90) & (ord(self.word[i]) + change >= 65) & (ord(self.word[i]) >= 65) & (ord(self.word[i]) <= 90):
                self.turned.append(chr(ord(self.word[i])+change))
            elif (ord(self.word[i]) + change <= 122) & (ord(self.word[i]) + change >= 97) & (ord(self.word[i]) >= 97) & (ord(self.word[i]) <= 122):
                self.turned.append(chr(ord(self.word[i])+change))
            elif (ord(self.word[i]) + change < 65) & (ord(self.word[i]) >= 65) & (ord(self.word[i]) <= 90):
                self.turned.append(chr(ord(self.word[i])+change + 26))
            elif (ord(self.word[i]) + change > 90) & (ord(self.word[i]) >= 65) & (ord(self.word[i]) <= 90):
                self.turned.append(chr(ord(self.word[i])+change - 26))
            elif (ord(self.word[i]) + change < 97) & (ord(self.word[i]) >= 97) & (ord(self.word[i]) <= 122):
                self.turned.append(chr(ord(self.word[i])+change + 26))
            elif (ord(self.word[i]) + change > 122) & (ord(self.word[i]) >= 97) & (ord(self.word[i]) <= 122):
                self.turned.append(chr(ord(self.word[i])+change - 26))
        print(''.join(self.turned))
    def turn(self,input1,change):
        self.input1 = input1
        self.change = change
        self.turned = []
        self.lenth = len(self.input1)
        for i in range(self.lenth):
            if (self.input1[i] ==  ' ') | (self.input1[i] ==  ',') | (self.input1[i] ==  '!') | (self.input1[i] ==  '.'):
                self.turned.append(self.input1[i])
            elif (ord(self.input1[i]) + change <= 90) & (ord(self.input1[i]) + change >= 65) & (ord(self.input1[i]) >= 65) & (ord(self.input1[i]) <= 90):
                self.turned.append(chr(ord(self.input1[i])+change))
            elif (ord(self.input1[i]) + change <= 122) & (ord(self.input1[i]) + change >= 97) & (ord(self.input1[i]) >= 97) & (ord(self.input1[i]) <= 122):
                self.turned.append(chr(ord(self.input1[i])+change))
            elif (ord(self.input1[i]) + change < 65) & (ord(self.input1[i]) >= 65) & (ord(self.input1[i]) <= 90):
                self.turned.append(chr(ord(self.input1[i])+change + 26))
            elif (ord(self.input1[i]) + change > 90) & (ord(self.input1[i]) >= 65) & (ord(self.input1[i]) <= 90):
                self.turned.append(chr(ord(self.input1[i])+change - 26))
            elif (ord(self.input1[i]) + change < 97) & (ord(self.input1[i]) >= 97) & (ord(self.input1[i]) <= 122):
                self.turned.append(chr(ord(self.input1[i])+change + 26))
            elif (ord(self.input1[i]) + change > 122) & (ord(self.input1[i]) >= 97) & (ord(self.input1[i]) <= 122):
                self.turned.append(chr(ord(self.input1[i])+change - 26))
        print(''.join(self.turned))
    def auto(self,input1):
        self.num = []
        self.output = []
        self.input1 = input1
        self.buffer = str.split(self.input1) # splited word
        self.lenth1 = len(self.buffer)# lenth1 is the number of word
        for i in range(self.lenth1):
            self.lenth = len(self.buffer[i])# lenth is the lenth of word
            for j in range(self.lenth):
                self.num.append(ord(self.buffer[i][j]))
                # self.num is the original ascii number of a word
            minum = sorted(self.num)# minum is a rank of original ascii number
            self.code = []# self.code is a number to ensure a word,clear the self.code
            for k in self.num:
                self.code.append(k-minum[0])
            self.lenth2 = len(self.dict1)
            for o in range(self.lenth2):
                if self.code == self.dict1[o]:
                    self.change = self.num[0] - self.code[0] - self.dict2[o]# self.change is the key
                    self.num = []#clear the self.num
        for l in range(self.lenth1):
            self.num = []#clear the self.num
            self.lenth = len(self.buffer[l])
            for m in range(self.lenth):
                self.num.append(ord(self.buffer[l][m]))#rebuild the self.num
            for n in range(self.lenth):
                if (self.num[n] == ord(' ')) | (self.num[n] == ord(',')) | (self.num[n] == ord('.')) | (self.num[n] == ord('!')):
                    self.output.append(chr(self.num[n]))
                elif (self.num[n] - self.change <= 90) & (self.num[n] - self.change >= 65) & (self.num[n] >= 65) & (self.num[n] <= 90):
                    self.output.append(chr(self.num[n] - self.change))
                elif (self.num[n] - self.change <= 122) & (self.num[n] - self.change >= 97) & (self.num[n] >= 97) & (self.num[n] <= 122):
                    self.output.append(chr(self.num[n] - self.change))
                elif (self.num[n] - self.change < 65) & (self.num[n] >= 65) & (self.num[n] <= 90):
                    self.output.append(chr(self.num[n] - self.change + 26))
                elif (self.num[n] - self.change > 90) & (self.num[n] >= 65) & (self.num[n] <= 90):
                    self.output.append(chr(self.num[n] - self.change - 26))
                elif (self.num[n] - self.change < 97) & (self.num[n] >= 97) & (self.num[n] <= 122):
                    self.output.append(chr(self.num[n] - self.change + 26))
                elif (self.num[n] - self.change > 122) & (self.num[n] >= 97) & (self.num[n] <= 122):
                    self.output.append(chr(self.num[n] - self.change - 26))
                    #self.output.append(chr(self.num[n] - self.change))
            self.output.append(' ')
        print(''.join(self.output))
n = caesar('Begin!')
n.turn('zkhq brx vhh wklv,brx duh vxffhvv!',-3)
n.turnw('zkhq',-3)
n.encode('apple')#append 'success' code to dict
n.auto('yjgp')
n.auto('dq dssoh') #bug
n.auto('zkhq brx vhh wklv,brx duh vxffhvv!')
