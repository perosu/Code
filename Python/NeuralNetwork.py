# neural network class definition
class neuralNetwork:
    
    # initialise the neural network
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        #set number of nodes in input,hidden and output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        # link weight matrices,wih,who
        #weights inside the  arrays are w_i_j,where link is from node i to node j in the next layer
        # w11 w21
        # w21 w22
        self.wih = (numpy.random.rand(self.hnodes,self.inodes) - 0.5)
        self.who = (numpy.random.rand(self.onodes,self.hnodes) - 0.5)
        
        #learning rate
        self.lr = learningrate
        pass
    
    # train the neural network
    def train():
        pass
    
    #query the neural network
    def query():
        pass
    pass
input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate = 0.5
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)
