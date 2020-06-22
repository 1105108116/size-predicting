from tkinter import *

#########################################################################################################################
# python notebook for Make Your Own Neural Network
# code for a 3-layer neural network, and code for learning the MNIST dataset
# (c) Tariq Rashid, 2016
# license is GPLv2
import numpy
# scipy.special for the sigmoid function expit()
import scipy.special
# library for plotting arrays
import matplotlib.pyplot
# ensure the plots are inside this notebook, not an external window
#%matplotlib inline
# neural network class definition

input_array = [0]*4


class neuralNetwork:
     # initialise the neural network
     def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
         # set number of nodes in each input, hidden, output layer
         self.inodes = inputnodes
         self.hnodes = hiddennodes
         self.onodes = outputnodes
         # link weight matrices, wih and who
         # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
         # w11 w21
         # w12 w22 etc
         self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
         self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
         # learning rate
         self.lr = learningrate
         # activation function is the sigmoid function
         self.activation_function = lambda x: scipy.special.expit(x)
         #pass
     # train the neural network
     def train(self, inputs_list, targets_list):
         # convert inputs list to 2d array
         inputs = numpy.array(inputs_list, ndmin=2).T
         targets = numpy.array(targets_list, ndmin=2).T
         # calculate signals into hidden layer
         hidden_inputs = numpy.dot(self.wih, inputs)
         # calculate the signals emerging from hidden layer
         hidden_outputs = self.activation_function(hidden_inputs)
         # calculate signals into final output layer
         final_inputs = numpy.dot(self.who, hidden_outputs)
         # calculate the signals emerging from final output layer
         final_outputs = self.activation_function(final_inputs)
         # output layer error is the (target - actual)
         output_errors = targets - final_outputs
         # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
         hidden_errors = numpy.dot(self.who.T, output_errors)
         # update the weights for the links between the hidden and output layers
         self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
         numpy.transpose(hidden_outputs))
         # update the weights for the links between the input and hidden layers
         self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 -
         hidden_outputs)),
         numpy.transpose(inputs))
         #pass
     # query the neural network
     def query(self, inputs_list):
         # convert inputs list to 2d array
         inputs = numpy.array(inputs_list, ndmin=2).T
         # calculate signals into hidden layer
         hidden_inputs = numpy.dot(self.wih, inputs)
         # calculate the signals emerging from hidden layer
         hidden_outputs = self.activation_function(hidden_inputs)
         # calculate signals into final output layer
         final_inputs = numpy.dot(self.who, hidden_outputs)
         # calculate the signals emerging from final output layer
         final_outputs = self.activation_function(final_inputs)
         return final_outputs
# number of input, hidden and output nodes
         
     
input_nodes = 4
hidden_nodes = 3
output_nodes = 11
# learning rate is 0.3
learning_rate = 0.3
# create instance of neural network
nn = neuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)

def NN_learning():
    # load the mnist training data CSV file into a list
    #請注意原始 mnist_train.csv 檔案第一列為 column name
    training_data_file = open("NN_final_train.csv", 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()
    # train the neural network;
    # epochs is the number of times the training data set is used for training
    epochs = 5
    for e in range(epochs):
         # go through all records in the training data set
         for record in training_data_list:
             # split the record by the ',' commas
             all_values = record.split(',')
             # scale and shift the inputs
             inputs = (numpy.asfarray(all_values[1:]) / 500.0 * 0.99) + 0.01
             # create the target output values (all 0.01, except the desired label which is 0.99)
             targets = numpy.zeros(output_nodes) + 0.01
             # all_values[0] is the target label for this record
             targets[int(all_values[0])] = 0.99
             nn.train(inputs, targets)
             pass
         pass
    # load the mnist test data CSV file into a list
#    test_data_file = open("exam_test.csv", 'r')
#    test_data_list = test_data_file.readlines()
#    test_data_file.close()



    scorecard = []
    # go through all the records in the test data set
    for i in input_array:
#         # split the record by the ',' commas
#         all_values = record.split(',')
#         # correct answer is first value
#         correct_label = int(all_values[0])
#         # scale and shift the inputs
         inputs = (numpy.asfarray(input_array[0:]) / 500.0 * 0.99) + 0.01
    
         # query the network
         outputs = nn.query(inputs)
         # the index of the highest value corresponds to the label
         label = numpy.argmax(outputs)
         scorecard.append(label)
         # append correct or incorrect to list
    #      if (label == correct_label):
    #          # network's answer matches correct answer, add 1 to scorecard
    #          scorecard.append(1)
    #      else:
    #          # network's answer doesn't match correct answer, add 0 to scorecard
    #          scorecard.append(0)
    #          pass
    #      pass
    # calculate the performance score, the fraction of correct answers
    scorecard_array = numpy.asarray(scorecard)
    print ("score = ", scorecard[0])

#########################################################################################################################
    
class window:
    def __init__(self):
        # create a tkinter window
        self.win = Tk()

        #reset the window and baackground color
        self.canvas = Canvas(self.win,
                             width=1600, height=1200,
                             bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        #show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width/2-600/2)
        y = int(height/2-400/2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        #disable resize of the window
        self.win.resizable(width=False, height=False)

        #change the title of the window
        self.win.title("尺寸預測")

    def add_frame(self):
        #create a inner frame
        self.frame = Frame(self.win, height=600, width=750)
        self.frame.place(x=0, y=0)

        x, y = 70, 20
        #self.img = PhotoImage("T-shirt.jpg")
        #self.label = Label(self.frame, image=self.img)
        #self.label.place(x=x-30, y=y-10)
        
        
            ######################################################## predict_size
        self.size_label = Label(self.frame, text="適合尺寸:")
        self.size_label.config(font=("Courier", 12, 'bold'))
        self.size_label.place(x=x+100, y=y+320)
        
        self.predict_label = Label(self.frame, text="預測結果")
        self.predict_label.config(font=("Courier", 12, 'bold'))
        self.predict_label.place(x=x+200, y=y+320)
        
        
        
        
        
        self.topiclabel = Label(self.frame, text="輸入資料")
        self.topiclabel.config(font=("Courier", 20, 'bold'))
        self.topiclabel.place(x=x+170, y=y)
        
            ######################################################## height   
        self.height_label = Label(self.frame, text="輸入身高:")
        self.height_label.config(font=("Courier", 12, 'bold'))
        self.height_label.place(x=x+50, y=y+70)

        self.height_input = Entry(self.frame, font='Courier 12')
        self.height_input.place(x=x+150, y=y+70)
        
            
            ######################################################## weight
        self.weight_label = Label(self.frame, text="輸入體重:")
        self.weight_label.config(font=("Courier", 12, 'bold'))
        self.weight_label.place(x=x+50, y=y+110)

        self.weight_input = Entry(self.frame,font='Courier 12')
        self.weight_input.place(x=x+150, y=y+110)   

        
            ######################################################## width
        self.width_label = Label(self.frame, text="輸入肩寬:")
        self.width_label.config(font=("Courier", 12, 'bold'))
        self.width_label.place(x=x+50, y=y+150)

        self.width_input = Entry(self.frame, font='Courier 12')
        self.width_input.place(x=x+150, y=y+150)
        
        
            ######################################################## bust
        self.bust_label = Label(self.frame, text="輸入胸圍:")
        self.bust_label.config(font=("Courier", 12, 'bold'))
        self.bust_label.place(x=x+50, y=y+190)

        self.bust_input = Entry(self.frame, font='Courier 12')
        self.bust_input.place(x=x+150, y=y+190)     
        
        
            ######################################################## predict_buttton
            
        self.button = Button(self.frame, text="預測",
                            font=('helvetica', 20, 'underline italic'),
                            bg='dark blue', fg='white',command=self.NN_predict)
        self.button.place(x=x+200, y=y+240)    
            
            
        

        
        self.win.mainloop()
        
        
        
    def NN_predict(self):
        input_array[0] = int(self.height_input.get())
        input_array[1] = int(self.weight_input.get())
        input_array[2] = int(self.width_input.get())
        input_array[3] = int(self.bust_input.get())
        NN_learning()
    
    
    
    
    
    
    
    
    
def main(self):
        x = window()
        x.add_frame()
        
        


if __name__ == "__main__":
    main(0)