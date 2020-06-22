from tkinter import *

#導入TensorFlow套件
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import time
import csv


################################################################################
training_data_file = open("NN_final_train.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

training_data_items = 16
x_train =[[0]*5 for i in range(training_data_items)]

x=0
for record in training_data_list:
    # split the record by the ',' commas
    all_values = record.split(',')
    for i in range(5):
        if x < training_data_items:
            x_train[x][i]= int(all_values[i])
    x+=1
    pass
 
################################################################################    
#開始計時
start = time.time()
#定義三個預留位置，資料類型為浮點型
x1 = tf.placeholder(dtype=tf.float32)
x2 = tf.placeholder(dtype=tf.float32)
x3 = tf.placeholder(dtype=tf.float32)
x4 = tf.placeholder(dtype=tf.float32)
#增加一個目標值
yTrain = tf.placeholder(dtype=tf.float32)
 
#定義三個可變參數，資料類型為浮點型
w1 = tf.Variable(0.01, dtype=tf.float32)
w2 = tf.Variable(0.01, dtype=tf.float32)
w3 = tf.Variable(0.01, dtype=tf.float32)
w4 = tf.Variable(0.01, dtype=tf.float32)
wn = [w1, w2, w3, w4]
 
n1 = x1 * wn[0]
n2 = x2 * wn[1]
n3 = x3 * wn[2]
n4 = x4 * wn[3]
y = n1 + n2 + n3 + n4
 
#訓練值和目標值的絕對值差
loss = tf.abs(y - yTrain)
 
#使用RMSPropOptimzer優化器
optimizer = tf.train.RMSPropOptimizer(0.0001)  #可以改為0.0001執行
#依照最小化的原則處理loss
train = optimizer.minimize(loss)
 
#會話物件
sess = tf.Session()
#初始化可變參數
init = tf.global_variables_initializer()
sess.run(init)
 
loopNum = 500 #計算迴圈次數，可以改為50000執行

json_file = open('learning_architecture.json', 'w')
save_weights_file = open("save_weights.csv", 'w')
writer = csv.writer(save_weights_file)

for i in range(loopNum):
    #print("* %d / %d" % (i+1,loopNum))  #顯示目前迴圈次數
    json_file.write("* %d / %d" % (i+1,loopNum))
    #輸出要查看的變數與餵資料
    for j in range(training_data_items):
        
        result = sess.run([train, x1, x2, x3, x4, w1, w2, w3, w4, wn, y, yTrain, loss],
                          feed_dict={x1: x_train[j][1], x2: x_train[j][2], x3: x_train[j][3], x4: x_train[j][4], yTrain: x_train[j][0]})

       # print(str(result[5])+" "+str(result[6])+" "+str(result[7])+" "+str(result[8]))
        #print(result[9])
        json_file.write("".join(str(result[9])))
    #print("-" * 100)
    json_file.write("-" * 100 + "\n")

writer.writerow([result[9][0],result[9][1],result[9][2],result[9][3]])
save_weights_file.close()    
json_file.close()

#結束計時
end = time.time()
#顯示計算耗費時間
print("* Cost Time:", end-start)







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
        hight = float(self.height_input.get())
        weight = float(self.weight_input.get())
        width = float(self.width_input.get())
        bust = float(self.bust_input.get())
        #self.predict_label.configure(text=hight+weight+width+bust)
        
        save_weights_file = open("save_weights.csv", 'r')
        save_weights = save_weights_file.readlines()
        save_weights = ''.join(save_weights).strip('\n')
        save_weights_file.close()
        
        values = save_weights.split(',')
        
        predict_size = (hight*float(values[0]))+(weight*float(values[1]))+(width*float(values[2]))+(bust*float(values[3]))
        
        size_to_show = round(predict_size,0)
        if size_to_show == 1:
            self.predict_label.configure(text = "S")
        elif size_to_show == 2:
            self.predict_label.configure(text = "M")
        elif size_to_show == 3:
            self.predict_label.configure(text = "L")
        elif size_to_show == 4:
            self.predict_label.configure(text = "XL")
        elif size_to_show == 5:
            self.predict_label.configure(text = "XXL")
        else:
            self.predict_label.configure(text = "數值錯誤")
        print(predict_size)
        print(size_to_show)
def main(self):
        x = window()
        x.add_frame()
        
        


if __name__ == "__main__":
    main(0)