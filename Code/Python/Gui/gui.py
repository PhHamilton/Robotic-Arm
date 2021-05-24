import tkinter as tk
from tkinter import Canvas, DoubleVar, Scale, Widget, mainloop, ttk
from tkinter.constants import ANCHOR

from PIL import Image, ImageTk
import time

import math


class gui():
    def __init__(self):
        self.numberOfEntries = 0
        self.position = 0
        
        self.initGui()
        self.create_RobotMotion_Widget()
        self.create_StoredValues_Widget()
        self.create_RobotMotionIllustration_Widget()



    def initGui(self):
        self.root = tk.Tk()
        self.row0Height = 100
        self.row1Height = 300
        self.row2Height = 200
        self.column0Width = 300
        self.column1Width = 500

        self.width = 1280 #self.column0Width + self.column1Width
        self.height = 720 #self.row0Height + self.row1Height + self.row2Height
        self.padding = 5
        self.root.geometry('{}x{}'.format(self.width, self.height+2*self.padding))
        # self.root.resizable(False, False)
        self.root.title("Robotic Arm GUI")


    def create_RobotMotion_Widget(self):
        # Motion Frame
        #----------------------------------#
        MotionFrame = ttk.LabelFrame(self.root, text = "Robot Motion")
        MotionFrame.grid(row=0, column=0, padx=self.padding, pady=self.padding, sticky="nesw")
        AutoFrame = ttk.LabelFrame(MotionFrame, text='Auto Mode')
        AutoFrame.grid(row=1, column=0, padx=self.padding, pady=self.padding, sticky="nesw")
        SemiAutoFrame = ttk.LabelFrame(MotionFrame, text='Semi Auto Mode')
        SemiAutoFrame.grid(row=2, column=0, padx=self.padding, pady=self.padding, sticky="nesw")
        manualFrame = ttk.LabelFrame(MotionFrame, text='Manual')
        manualFrame.grid(row=1, column=1, rowspan=2, padx=self.padding, pady=self.padding, sticky="nesw")

        defaultButton = ttk.Button(AutoFrame, text="Default Position")
        defaultButton.grid(row=0,column=0, sticky="NESW")

        pointForwardButton = ttk.Button(AutoFrame, text = "Point Forward")
        pointForwardButton.grid(row=1, column=0, sticky ="nesw")

        pointBackwardButton = ttk.Button(AutoFrame, text = "Point Backward")
        pointBackwardButton.grid(row=2, column=0, sticky ="nesw")
        

        homeButton = ttk.Button(SemiAutoFrame, text="Home")
        homeButton.grid(row=0,column=0, columnspan=2, sticky="NESW")
        rotateButton = ttk.Button(SemiAutoFrame, text="Rotate 45 degrees")
        rotateButton.grid(row=1, column=0, columnspan=2, sticky="NESW")

        self.radioChoice = tk.IntVar()
        self.radioChoice.set(0)
        radioCW = ttk.Radiobutton(SemiAutoFrame, variable = self.radioChoice, value=0)
        radioCW.grid(row=3,column=0)
        CWText = ttk.Label(SemiAutoFrame, text = "CW")
        CWText.grid(row=4, column=0)
        
        radioCCW = ttk.Radiobutton(SemiAutoFrame, variable = self.radioChoice, value=1)
        radioCCW.grid(row=3,column=1)
        CCWText = ttk.Label(SemiAutoFrame, text = "CCW")
        CCWText.grid(row=4, column=1)

        gripperLabel = ttk.Label(SemiAutoFrame, text="Gripper")
        gripperLabel.grid(row=5, column=0, columnspan=2)
        openButton = ttk.Button(SemiAutoFrame, text="Open")
        openButton.grid(row=6, column=0)
        closeButton = ttk.Button(SemiAutoFrame, text="Close")
        closeButton.grid(row=6, column=1)

        test = ttk.Label(manualFrame, text="Join Position")
        test.grid(row=0, column=0)
    
        # Axis 0
        self.axis0Val = tk.DoubleVar()
        self.axis0 = ttk.Scale(manualFrame, var = self.axis0Val, command=self.updateTextBox, from_=0, to=10,orient=tk.HORIZONTAL)
        self.axis0.grid(row=1,column=0, sticky="w")

        self.axis0textBox = ttk.Entry(manualFrame, width = 5)
        self.axis0textBox.grid(column=1, row=1, sticky = tk.W)
        self.axis0textBox.insert(0,"0")
        self.axis0textBox.bind("<Return>", self.onReturn)
        

        self.axis1Val = tk.DoubleVar()
        self.axis1 = ttk.Scale(manualFrame, var = self.axis1Val, command = self.updateTextBox, from_=-50, to=55,orient=tk.HORIZONTAL)
        self.axis1.grid(row=2,column=0, sticky="w")

        self.axis1textBox = ttk.Entry(manualFrame, width = 5)
        self.axis1textBox.grid(column=1, row=2, sticky = tk.W)
        self.axis1textBox.insert(0,"0")
        self.axis1textBox.bind("<Return>", self.onReturn)

        self.axis2Val = tk.DoubleVar()
        self.axis2 = ttk.Scale(manualFrame, var = self.axis2Val, command = self.updateTextBox, from_=-50, to=55,orient=tk.HORIZONTAL)
        self.axis2.grid(row=3,column=0, sticky="w")

        self.axis2textBox = ttk.Entry(manualFrame, width = 5)
        self.axis2textBox.grid(column=1, row=3, sticky = tk.W)
        self.axis2textBox.insert(0,"0")
        self.axis2textBox.bind("<Return>", self.onReturn)

        self.axis3Val = tk.DoubleVar()
        self.axis3 = ttk.Scale(manualFrame, var = self.axis3Val, command = self.updateTextBox, from_=-50, to=55,orient=tk.HORIZONTAL)
        self.axis3.grid(row=4,column=0, sticky="w")

        self.axis3textBox = ttk.Entry(manualFrame, width = 5)
        self.axis3textBox.grid(column=1, row=4, sticky = tk.W)
        self.axis3textBox.insert(0,"0")
        self.axis3textBox.bind("<Return>", self.onReturn)

        # Axis 4

        self.axis4Val = tk.DoubleVar()
        self.axis4 = ttk.Scale(manualFrame, var = self.axis4Val, command = self.updateTextBox, from_=0, to=10,orient=tk.HORIZONTAL)
        self.axis4.grid(row=5,column=0, sticky="w")

        self.axis4textBox = ttk.Entry(manualFrame, width = 5)
        self.axis4textBox.grid(column=1, row=5, sticky = tk.W)
        self.axis4textBox.insert(0,"0")
        self.axis4textBox.bind("<Return>", self.onReturn)

        saveButton = ttk.Button(manualFrame, command=self.saveValue, text="Save")
        saveButton.grid(row=6,column=0)
        clearButton = ttk.Button(manualFrame, command=self.clearTextBox, text="Clear")
        clearButton.grid(row=7,column=0)

        goButton = ttk.Button(manualFrame, text="Go", width = 2)
        goButton.grid(row=6,column=1, rowspan=2, sticky="SN")

    def create_StoredValues_Widget(self):
        StoredValueFrame = ttk.LabelFrame(self.root)
        StoredValueFrame.grid(row=1, column=0, padx=self.padding, pady=self.padding, sticky="nesw")

        textFrame = ttk.LabelFrame(StoredValueFrame, text = "Stored Values")
        textFrame.grid(row=0,column=0,padx = self.padding, sticky="nesw")

        self.saveValueBox= tk.Text(textFrame, width = 30, height = 10)
        self.saveValueBox.grid(row=0, column = 0, sticky="nesw")

        upDownFrame = ttk.LabelFrame(StoredValueFrame)
        upDownFrame.grid(row=0, column=1, padx=20, sticky="nesw")
        
        upArrowButton = ttk.Button(upDownFrame,command = lambda:self.moveSelector(-1), text="Up")

        upArrowButton.grid(row=0, column=0, sticky="NW")

        clearButton = ttk.Button(upDownFrame, command=self.removeEntry, text="Clear")
        clearButton.grid(row=1, column=0, sticky="W")

        downArrowButton = ttk.Button(upDownFrame, command = lambda:self.moveSelector(1), text="Down")
        downArrowButton.grid(row=2, column=0, sticky="SW")

        emptyLabel = ttk.Label(upDownFrame)
        emptyLabel.grid(row=3, column=0)

        clearAllButton = ttk.Button(upDownFrame, command = self.clearAllEntries, text="Clear All")
        clearAllButton.grid(row=5, column=0, sticky="S")

        f = tk.Frame(relief='flat')
        # lF = ttk.LabelFrame(root, labelwidget=f, borderwidth=4)

        saveLoadFrame = ttk.Frame(StoredValueFrame)
        saveLoadFrame.grid(row=1, column=0, padx=self.padding, )#, sticky="nesw")
        
        loadButton = ttk.Button(saveLoadFrame, command = self.loadEntry, text="Load",width = 20)
        loadButton.grid(row=0, column=0)


    def create_RobotMotionIllustration_Widget(self):
        motionIllustration = ttk.LabelFrame(self.root, text = "Illustration", width = 600 + 2*self.padding, height =400 + 2*self.padding)
        motionIllustration.grid(row = 0, column = 1, rowspan=2, padx= self.padding, pady = self.padding)

        self.a = app(motionIllustration, 1200, 800, 1)
        # canvas = tk.Canvas(motionIllustration, width = 600, height = 400, bg="black")
        # canvas.grid(sticky="nesw")



        



    def clearAllEntries(self):
        self.saveValueBox.delete("0.0",tk.END)
        self.numberOfEntries = 0
        
    def loadEntry(self):
        if(self.numberOfEntries < 1):
            return
        value = tk.StringVar()
        value = self.saveValueBox.get('{}.{}'.format(self.position,0), '{}.{}{}'.format(self.position+1,0,"-1c"))
        
        self.axis0Val.set(int(value[1]))
        self.axis1Val.set(int(value[3]))
        self.axis2Val.set(int(value[5]))
        self.axis3Val.set(int(value[7]))
        self.axis4Val.set(int(value[9]))

        self.updateTextBox()
     
    def removeEntry(self):
        if(self.numberOfEntries > 0):
            self.numberOfEntries -= 1
            self.saveValueBox.delete('{}.{}'.format(self.position,0), '{}.{}'.format(self.position+1,0))
            self.moveSelector(-1)
        if(self.numberOfEntries == 0):
            self.saveValueBox.tag_remove(tk.SEL, "0.0", "1.0") 
            self.firstEntry = True        

    def moveSelector(self, pos):
        self.position = self.position + pos   
    
        if(self.position < 1):
            self.position = 1
        
        if(self.position > self.numberOfEntries):
            self.position = self.numberOfEntries 

            

        self.setSelector(self.position)  

    def setSelector(self, pos):
        self.saveValueBox.tag_remove(tk.SEL, '{}.{}'.format(pos-1,0), '{}.{}'.format(pos,0))
        self.saveValueBox.tag_remove(tk.SEL, '{}.{}'.format(pos+1,0), '{}.{}'.format(pos+2,0))
        self.saveValueBox.tag_add(tk.SEL, '{}.{}'.format(pos,0), '{}.{}'.format(pos+1,0))
        self.saveValueBox.mark_set(tk.INSERT, '{}.{}'.format(pos,0))
        self.saveValueBox.see(tk.INSERT)
        # self.console.tag_add(tk.SEL, "1.0", tk.END)
        # self.console.mark_set(tk.INSERT, "1.0")
        # self.console.see(tk.INSERT)
        
    def saveValue(self):
        # self.console.config(state = tk.NORMAL)
        # self.console.insert(tk.END, "{}{}".format(int(self.value.get()),"\n"))
        self.saveValueBox.insert("1.0", "({},{},{},{},{}){}".format(int(self.axis0Val.get()), int(self.axis1Val.get()), int(self.axis2Val.get()), int(self.axis3Val.get()), int(self.axis4Val.get()), "\n"))
        self.numberOfEntries += 1
        
        self.moveSelector(1)
    
    def clearTextBox(self):
        self.axis0Val.set(0)
        self.axis1Val.set(0)
        self.axis2Val.set(0)
        self.axis3Val.set(0)
        self.axis4Val.set(0)

        self.axis0.set(str(self.axis0Val.get()))
        self.axis1.set(str(self.axis1Val.get()))
        self.axis2.set(str(self.axis2Val.get()))
        self.axis3.set(str(self.axis3Val.get()))
        self.axis4.set(str(self.axis4Val.get()))

        self.updateTextBox()

    def onReturn(self, entry):
        axis0 = tk.StringVar()
        axis0 = self.axis0textBox.get()

        axis1 = tk.StringVar()
        axis1 = self.axis1textBox.get()

        axis2 = tk.StringVar()
        axis2 = self.axis2textBox.get()

        axis3 = tk.StringVar()
        axis3 = self.axis3textBox.get()

        axis4 = tk.StringVar()
        axis4 = self.axis4textBox.get()

    
        self.axis0.set(axis0)
        self.axis1.set(axis1)
        self.axis2.set(axis2)
        self.axis3.set(axis3)
        self.axis4.set(axis4)

    def updateTextBox(self, val = None):
        
        self.axis0textBox.delete(0, tk.END)
        self.axis0textBox.insert(0,str(int(self.axis0Val.get())))

        self.axis1textBox.delete(0, tk.END)
        self.axis1textBox.insert(0,str(int(self.axis1Val.get())))

        self.axis2textBox.delete(0, tk.END)
        self.axis2textBox.insert(0,str(int(self.axis2Val.get())))

        self.axis3textBox.delete(0, tk.END)
        self.axis3textBox.insert(0,str(int(self.axis3Val.get())))

        self.axis4textBox.delete(0, tk.END)
        self.axis4textBox.insert(0,str(int(self.axis4Val.get())))

        self.a.updateImage(int(self.axis1Val.get()),int(self.axis2Val.get()),int(self.axis3Val.get()))

    def directionSelection(self):
        return self.radioChoice.get()    

    def run(self):
        self.root.mainloop()        




def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

def toRad(deg):
    return deg*math.pi/180    

def sin(deg):
    return math.sin(toRad(deg))    

def cos(deg):
    return math.cos(toRad(deg))        


# root = tk.Tk()
# root.geometry("400x800")



# x0 = 200
# y0 = 650


# angle = 0
# angle2 = 0
# angle3 = 0

# canvas = tk.Canvas(width=800, height=800, bg='black')

# # pack the canvas into a frame/form
# canvas.pack(expand=tk.YES, fill=tk.BOTH)

# raw_image = Image.open('Images/Axis1.png')
# raw_image = raw_image.resize((142,127))
# my_img = ImageTk.PhotoImage(raw_image)


# raw_image2 = Image.open('Images/Axis2.png')
# raw_image2 = raw_image2.resize((142,188))
# raw_image2 = raw_image2.rotate(angle, expand = tk.TRUE)
# my_img2 = ImageTk.PhotoImage(raw_image2)

# raw_image3 = Image.open('Images/Axis3.png')
# raw_image3 = raw_image3.resize((142,188))
# raw_image3 = raw_image3.rotate(angle2, expand = tk.TRUE)
# my_img3 = ImageTk.PhotoImage(raw_image3)

# raw_image4 = Image.open('Images/Axis4AndEndeffector.png')
# # raw_image4 = raw_image4.resize((142,156))
# raw_image4 = raw_image4.resize((142,316))
# raw_image4 = raw_image4.rotate(angle3, expand = tk.TRUE)
# my_img4 = ImageTk.PhotoImage(raw_image4)


# raw_image5 = Image.open('Images/EndEffector.png')
# raw_image5 = raw_image5.resize((142,148))
# raw_image5 = raw_image5.rotate(angle3, expand = tk.TRUE)
# my_img5 = ImageTk.PhotoImage(raw_image5)

# # load the .gif image file


# # put gif image on canvas
# # pic's upper left corner (NW) on the canvas is at x=50 y=10

# l = 60#60
# l2 = 60#60
# l3 = 136 #342-206 # 354-206
# l4 = 121
# l5 = 138 #206-70

# l6 = 80
# l7 = 184

# SolvesFirstAngle_X = x0 -(l2+l3-l)*sin(angle)# - l2*sin(angle2)
# SolvesSecondAngle_X = -l5*sin(angle2)
# SolvesThirdAngle_X = -l4*sin(angle3)#l2*sin(angle2) + l4*sin(angle3)


# SolvesFirstAngle_Y = y0-254-120 + (l2+l3-l)*(1-cos(angle))
# SolvesSecondAngle_Y = l5*(1-cos(angle2))
# SolvesThirdAngle_Y = l4*(1-cos(angle3))


# canvas.create_image(x0, y0, image=my_img)
# canvas.create_image(x0 -l*sin(angle), y0-117+11 +l*(1-cos(angle)), image=my_img2)
# canvas.create_image(x0 -(l2+l3-l)*sin(angle)-l2*sin(angle2), y0-254 + 12+ (l2+l3-l)*(1-cos(angle)) + l2*(1-cos(angle2)), image=my_img3)
# canvas.create_image(x0 -(l2+l3-l)*sin(angle) -l5*sin(angle2) -l4*sin(angle3),y0-254-120 -70+3+(l2+l3-l)*(1-cos(angle)) + l5*(1-cos(angle2))+l4*(1-cos(angle3)), image=my_img4)

# # root.mainloop()
# #######################################################################################
# lastAngle_X = 0#-l7*sin(angle3) + (l6-l4)*sin(angle3)
# lastAnlge_Y = 0#l7*(1-cos(angle3)) -(l6-l4)
# ####################################################################################### 
# # canvas.create_image(SolvesFirstAngle_X + SolvesSecondAngle_X + SolvesThirdAngle_X + lastAngle_X ,SolvesFirstAngle_Y -140 + SolvesSecondAngle_Y+SolvesThirdAngle_Y+lastAnlge_Y, image=my_img5)


# create_circle(x0, y0-104 ,5, canvas) #545
# create_circle(x0, y0-242 ,5, canvas) #408
# # create_circle(x0, y0-362 ,5, canvas) #288
# create_circle(x0, y0-254-120 -70+3 ,5, canvas) #148


# # canvas.create_image(x0,1, image=my_img3)

# create_circle(x0, 250 + 342 + 11, 10, canvas)
# create_circle(x0, 250 + 206+12, 10, canvas)
# create_circle(x0, 250 + 70+10, 10, canvas)         
# # create_circle(x0, y0-254-120 - 78 + 11, 10, canvas) 

# print("Circle 1: {}, Small Circle: {}".format(250 + 342 + 11, y0-106))
# print("Circle 2: {}, Small Circle: {}".format(250 + 206+12, y0-242))
# print("Circle 3: {}, Small Circle: {}".format(250 + 70+10, y0-254-120 -70+3))


# # 250+70 - (650 - 254 - 120 - 148) = 44

# root.mainloop()

class app():
    def __init__(self, root, Width, Height, scale):
        self.scale = scale
        self.canvas = tk.Canvas(root, width = Width, height = Height, bg="black")
        self.canvas.grid()
        # self.canvas.grid(row=0,column=0,sticky="nesw")
        # self.canvas.pack()#(expand=tk.YES, fill=tk.BOTH)

        self.x0 = 550
        self.y0 = 680

        self.l1 = 60
        self.l2 = 60
        self.l3 = 136
        self.l4 = 121
        self.l5 = 138


        self.armOffset_X = 50
        self.armOffset_Y = -75
        self.axis2Offset = -105 + self.armOffset_Y
        self.axis3Offset = -242 + self.armOffset_Y
        self.axis4Offset = -441 + self.armOffset_Y
        

        

        # raw_image = Image.open('Images/Axis1.png')
        # raw_image = raw_image.resize((172,157))
        # self.my_img = ImageTk.PhotoImage(raw_image)
        # self.canvas.create_image(self.x0, self.y0, image=self.my_img)
        self.loadImages()
        self.base  = self.scaleImage(self.base,0)
        self.axis1 = self.scaleImage(self.axis1,1)
        self.axis2 = self.scaleImage(self.axis2,2)
        self.axis3 = self.scaleImage(self.axis3,3)
        self.axis4 = self.scaleImage(self.axis4,4)
    
        
        self.updateImage(0, 0, 0)

        

    def loadImages(self):
        self.base  = Image.open('Images/Base.png')
        self.axis1 = Image.open('Images/Axis1.png')
        self.axis2 = Image.open('Images/Axis2.png')
        self.axis3 = Image.open('Images/Axis3.png')
        self.axis4 = Image.open('Images/Axis4AndEndeffector.png')
        

    def scaleImage(self, image, axis = None):
        if axis == 0: 
            return image.resize((round(self.scale*481),round(self.scale*127))) 
        elif axis == 1: 
            return image.resize((round(self.scale*142),round(self.scale*126))) 
        elif axis == 2 or axis == 3:
            return image.resize((round(self.scale*142),round(self.scale*188)))
        elif axis == 4: 
            return image.resize((round(self.scale*142),round(self.scale*316)))
        elif axis == 5:
            return image.resize((round(self.scale*142),round(self.scale*148)))
        else:
            return "Error"

        

    def createTkImage(self, image):
        return ImageTk.PhotoImage(image)

    def rotateImage(self, image, rotation):
        return image.rotate(rotation, expand = tk.TRUE)   

    def createImage(self, x, y, Image):
        return self.canvas.create_image(x, y, image = Image)

    def updateImage(self, Angle1, Angle2, Angle3):    
        self.baseTK = self.createTkImage(self.base)
        self.createImage(self.x0, self.y0, self.baseTK)

        self.axis1TK = self.createTkImage(self.rotateImage(self.axis1, 0))
        
        
        self.axis2TK = self.createTkImage(self.rotateImage(self.axis2, Angle1))
        self.createImage(self.x0 + self.armOffset_X -self.l1*self.sin(Angle1), self.y0 + self.axis2Offset + self.l1*(1-self.cos(Angle1)), self.axis2TK)

        self.createImage(self.x0 + self.armOffset_X,self.y0 + self.armOffset_Y, self.axis1TK)

        self.axis3TK = self.createTkImage(self.rotateImage(self.axis3, Angle2))
        self.createImage(self.x0 + self.armOffset_X-(self.l2+self.l3-self.l1)*self.sin(Angle1)-self.l2*self.sin(Angle2), self.y0 + self.axis3Offset +(self.l2+self.l3-self.l1)*(1-self.cos(Angle1)) + self.l2*(1-self.cos(Angle2)), self.axis3TK)

        self.axis4TK = self.createTkImage(self.rotateImage(self.axis4, Angle3))
        self.createImage(self.x0 + self.armOffset_X-(self.l2+self.l3-self.l1)*self.sin(Angle1) -self.l5*self.sin(Angle2) -self.l4*self.sin(Angle3),self.y0 + self.axis4Offset +(self.l2+self.l3-self.l1)*(1-self.cos(Angle1)) + self.l5*(1-self.cos(Angle2))+self.l4*(1-self.cos(Angle3)), self.axis4TK)

        

        

    def toRad(self, deg):
        return deg*math.pi/180    

    def sin(self, deg):
        return math.sin(toRad(deg))    

    def cos(self, deg):
        return math.cos(toRad(deg))            



a = gui()

a.run()

# root = tk.Tk()
# root.geometry("1200x800")

# a = app(root, 1200, 800, 1)
# a.updateImage(0,0,0)

# root.mainloop()