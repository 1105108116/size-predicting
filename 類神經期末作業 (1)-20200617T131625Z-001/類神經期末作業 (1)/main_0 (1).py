from tkinter import *



    
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
        hight = int(self.height_input.get())
        weight = int(self.weight_input.get())
        width = int(self.width_input.get())
        bust = int(self.bust_input.get())
#        self.predict_label.configure(text=hight+weight+width+bust)
        return(height,weight,width,bust)
    
def main(self):
        x = window()
        x.add_frame()
        
        


if __name__ == "__main__":
    main(0)