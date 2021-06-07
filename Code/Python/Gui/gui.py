import tkinter as tk
from tkinter import Canvas, DoubleVar, Scale, Widget, mainloop, ttk
from tkinter.constants import ANCHOR

from PIL import Image, ImageTk
from Classes.visualizataionApp import sideView, topView, frontView
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
        self.create_Console_Widget()



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
        MotionFrame.grid(row=0, column=0, padx=4*self.padding, pady=self.padding, sticky="nesw")

        AutoFrame = ttk.LabelFrame(MotionFrame, text="Auto Mode")
        AutoFrame.grid(row=2, column=0, columnspan=2, padx=self.padding, pady=self.padding, sticky="nesw")

        SemiAutoFrame = ttk.LabelFrame(MotionFrame, text='Semi Auto Mode')
        SemiAutoFrame.grid(row=1, column=0, padx=self.padding, pady=self.padding, sticky="nesw")

        manualFrame = ttk.LabelFrame(MotionFrame, text='Manual')
        manualFrame.grid(row=1, column=1, padx=self.padding, pady=self.padding, sticky="nesw")

        waveButton = ttk.Button(AutoFrame, text="Wave")
        waveButton.grid(row=0,column=0, sticky="NESW")

        stretchButton = ttk.Button(AutoFrame, text="Stretch")
        stretchButton.grid(row=0,column=1, sticky="NESW")

        # TimeBox
        timeLabel = ttk.Label(manualFrame, text="Time [s]")
        timeLabel.grid(row=6, column=0)
        self.timeVal = DoubleVar()

        self.time = ttk.Scale(manualFrame, var = self.timeVal, command = self.updateTextBox, from_=1, to=10, orient=tk.HORIZONTAL)
        self.time.set(1)
        self.time.grid(row= 7, column=0)
        
        self.timeBox = ttk.Entry(manualFrame, width = 5)
        self.timeBox.grid(column=1, row=7, sticky = "W")
        self.timeBox.insert(0, "1")
        self.timeBox.bind("<Return>", self.onReturn)

        saveButton = ttk.Button(manualFrame, command=self.saveValue, text="Save")
        saveButton.grid(row=8,column=0)
        clearButton = ttk.Button(manualFrame, command=self.clearTextBox, text="Clear")
        clearButton.grid(row=9,column=0)

        goButton = ttk.Button(manualFrame, text="Go", command = self.sendCommand, width = 2)
        goButton.grid(row=8,column=1, rowspan=2, sticky="SN")
       
        # pointForwardButton = ttk.Button(AutoFrame, text = "Point Forward")
        # pointForwardButton.grid(row=1, column=0, sticky ="nesw")

        # pointBackwardButton = ttk.Button(AutoFrame, text = "Point Backward")
        # pointBackwardButton.grid(row=2, column=0, sticky ="nesw")
        

        homeButton = ttk.Button(SemiAutoFrame, text="Home")
        homeButton.grid(row=0,column=0, columnspan=2, sticky="NESW")

        defaultButton = ttk.Button(SemiAutoFrame, command =lambda:self.moveTo(self.axis0Val.get(),20,-54,-55,self.axis4Val.get(),self.timeVal.get()), text="Default Position")
        defaultButton.grid(row=1,column=0, columnspan=2, sticky="NESW")

        pointForwardButton = ttk.Button(SemiAutoFrame, command =lambda:self.moveTo(self.axis0Val.get(),0,-34,-55,self.axis4Val.get(),self.timeVal.get()),text = "Point Forward")
        pointForwardButton.grid(row=2, column=0, columnspan=2, sticky ="nesw")

        pointBackwardButton = ttk.Button(SemiAutoFrame, command =lambda:self.moveTo(self.axis0Val.get(),0,40,50,self.axis4Val.get(),self.timeVal.get()), text = "Point Backward")
        pointBackwardButton.grid(row=3, column=0, columnspan=2, sticky ="nesw")

        rotateButton = ttk.Button(SemiAutoFrame, command =lambda:self.moveTo(45,self.axis1Val.get(),self.axis2Val.get(),self.axis3Val.get(),self.axis4Val.get(),self.timeVal.get()),  text="Rotate 45 degrees")
        rotateButton.grid(row=4, column=0, columnspan=2, sticky="NESW")

        self.radioChoice = tk.IntVar()
        self.radioChoice.set(0)
        radioCW = ttk.Radiobutton(SemiAutoFrame, variable = self.radioChoice, value=0)
        radioCW.grid(row=5,column=0)
        CWText = ttk.Label(SemiAutoFrame, text = "CW")
        CWText.grid(row=6, column=0)
        
        radioCCW = ttk.Radiobutton(SemiAutoFrame, variable = self.radioChoice, value=1)
        radioCCW.grid(row=5,column=1)
        CCWText = ttk.Label(SemiAutoFrame, text = "CCW")
        CCWText.grid(row=6, column=1)

        gripperLabel = ttk.Label(SemiAutoFrame, text="Gripper")
        gripperLabel.grid(row=7, column=0, columnspan=2)
        openButton = ttk.Button(SemiAutoFrame, text="Open")
        openButton.grid(row=8, column=0)
        closeButton = ttk.Button(SemiAutoFrame, text="Close")
        closeButton.grid(row=8, column=1)

        test = ttk.Label(manualFrame, text="Joint Position")
        test.grid(row=0, column=0)
    
        # Axis 0
        self.axis0Val = tk.DoubleVar()
        self.axis0 = ttk.Scale(manualFrame, var = self.axis0Val, command=self.updateTextBox, from_=90, to=-90,orient=tk.HORIZONTAL)
        self.axis0.grid(row=1,column=0, sticky="w")

        self.axis0textBox = ttk.Entry(manualFrame, width = 5)
        self.axis0textBox.grid(column=1, row=1, sticky = tk.W)
        self.axis0textBox.insert(0,"0")
        self.axis0textBox.bind("<Return>", self.onReturn)
        

        self.axis1Val = tk.DoubleVar()
        self.axis1 = ttk.Scale(manualFrame, var = self.axis1Val, command = self.updateTextBox, from_=50, to=-55,orient=tk.HORIZONTAL)
        self.axis1.grid(row=2,column=0, sticky="w")

        self.axis1textBox = ttk.Entry(manualFrame, width = 5)
        self.axis1textBox.grid(column=1, row=2, sticky = tk.W)
        self.axis1textBox.insert(0,"0")
        self.axis1textBox.bind("<Return>", self.onReturn)

        self.axis2Val = tk.DoubleVar()
        self.axis2 = ttk.Scale(manualFrame, var = self.axis2Val, command = self.updateTextBox, from_=50, to=-55,orient=tk.HORIZONTAL)
        self.axis2.grid(row=3,column=0, sticky="w")

        self.axis2textBox = ttk.Entry(manualFrame, width = 5)
        self.axis2textBox.grid(column=1, row=3, sticky = tk.W)
        self.axis2textBox.insert(0,"0")
        self.axis2textBox.bind("<Return>", self.onReturn)

        self.axis3Val = tk.DoubleVar()
        self.axis3 = ttk.Scale(manualFrame, var = self.axis3Val, command = self.updateTextBox, from_=50, to=-55,orient=tk.HORIZONTAL)
        self.axis3.grid(row=4,column=0, sticky="w")

        self.axis3textBox = ttk.Entry(manualFrame, width = 5)
        self.axis3textBox.grid(column=1, row=4, sticky = tk.W)
        self.axis3textBox.insert(0,"0")
        self.axis3textBox.bind("<Return>", self.onReturn)

        # Axis 4

        self.axis4Val = tk.DoubleVar()
        self.axis4 = ttk.Scale(manualFrame, var = self.axis4Val, command = self.updateTextBox, from_=90, to=-90,orient=tk.HORIZONTAL)
        self.axis4.grid(row=5,column=0, sticky="w")

        self.axis4textBox = ttk.Entry(manualFrame, width = 5)
        self.axis4textBox.grid(column=1, row=5, sticky = tk.W)
        self.axis4textBox.insert(0,"0")
        self.axis4textBox.bind("<Return>", self.onReturn)

        
    def create_StoredValues_Widget(self):
        StoredValueFrame = ttk.LabelFrame(self.root, text = "Stored Values")
        StoredValueFrame.grid(row=1, column=0, padx=4*self.padding, pady=self.padding, sticky="nesw")

        textFrame = ttk.LabelFrame(StoredValueFrame)
        textFrame.grid(row=0,column=0,padx = self.padding, sticky="nesw")

        self.saveValueBox= tk.Text(textFrame, width = 30, height = 10)
        self.saveValueBox.grid(row=0, column = 0, columnspan=2, sticky="nesw")

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



        saveLoadFrame = ttk.Frame(StoredValueFrame)
        saveLoadFrame.grid(row=1, column=0, padx=self.padding )#, sticky="nesw")
        
        loadButton = ttk.Button(saveLoadFrame, command = self.loadEntry, text="Load")
        loadButton.grid(row=0, column=0)

        self.loadAllFlag = tk.BooleanVar()
        self.loadAllFlag.set(tk.FALSE)
        loadAllButton = ttk.Button(saveLoadFrame, command = self.loadAllFlag.set(True), text ="Load all")
        loadAllButton.grid(row=0, column = 1)

    def create_RobotMotionIllustration_Widget(self):
        # motionIllustration = ttk.LabelFrame(self.root, text = "Illustration", width = 600 + 2*self.padding, height =400 + 2*self.padding)
        # motionIllustration.grid(row = 0, column = 1, padx= self.padding, pady = self.padding)
        motionIllustration = ttk.LabelFrame(self.root, text = "Illustration")
        motionIllustration.grid(row = 0, column = 1, padx= self.padding, pady = self.padding)
        sideViewFrame = ttk.Frame(motionIllustration)
        sideViewFrame.grid(row=0,column=0, rowspan = 2, padx= self.padding, pady = self.padding)
        topViewFrame = ttk.Frame(motionIllustration)
        topViewFrame.grid(row=0,column=1,padx= self.padding, pady = self.padding)
        frontViewFrame = ttk.Frame(motionIllustration)
        frontViewFrame.grid(row=1,column=1,padx= self.padding, pady = self.padding)
        

        self.a = sideView(sideViewFrame, 550, 380 + 4*self.padding, 0.5)
        self.b = topView(topViewFrame,200, 190, 0.5)
        self.c = frontView(frontViewFrame, 200, 190, 0.25)
        # canvas = tk.Canvas(motionIllustration, width = 600, height = 400, bg="black")
        # canvas.grid(sticky="nesw")

    def create_Console_Widget(self):
        consoleFrame = ttk.LabelFrame(self.root, text = "Console")
        consoleFrame.grid(row=1,column=1, padx = self.padding, pady = self.padding, sticky ="NESW")

        console = tk.Text(consoleFrame, width = 78, height = 14)
        console.grid(row=0,column=0, padx= self.padding, pady = self.padding)

    def moveTo(self, x0, x1, x2, x3, x4, time):
        if(self.radioChoice.get() == 1):
            self.axis0Val.set(x0)
        else:
            self.axis0Val.set(-x0)

        self.axis1Val.set(x1)
        self.axis2Val.set(x2)
        self.axis3Val.set(x3)
        self.axis4Val.set(x4)
        self.timeVal.set(time)
        self.updateTextBox()

    def clearAllEntries(self):
        self.saveValueBox.delete("0.0",tk.END)
        self.numberOfEntries = 0
        
    def loadEntry(self):
        if(self.numberOfEntries < 1):
            return
        
        intArray = self.getIntArray()
            



        self.axis0Val.set(intArray[0])
        self.axis1Val.set(intArray[1])
        self.axis2Val.set(intArray[2])
        self.axis3Val.set(intArray[3])
        self.axis4Val.set(intArray[4])
        self.timeVal.set(intArray[5])

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
        self.saveValueBox.insert("1.0", "({},{},{},{},{},{}){}".format(int(self.axis0Val.get()), int(self.axis1Val.get()), int(self.axis2Val.get()), int(self.axis3Val.get()), int(self.axis4Val.get()), int(self.timeVal.get()),"\n"))
        self.numberOfEntries += 1
        
        self.moveSelector(1)
    
    def clearTextBox(self):
        self.axis0Val.set(0)
        self.axis1Val.set(0)
        self.axis2Val.set(0)
        self.axis3Val.set(0)
        self.axis4Val.set(0)
        self.timeVal.set(1)

        self.axis0.set(str(self.axis0Val.get()))
        self.axis1.set(str(self.axis1Val.get()))
        self.axis2.set(str(self.axis2Val.get()))
        self.axis3.set(str(self.axis3Val.get()))
        self.axis4.set(str(self.axis4Val.get()))
        self.time.set(str(self.timeVal.get()))

        

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

        time = tk.StringVar()
        time = self.timeBox.get()

    
        self.axis0.set(axis0)
        self.axis1.set(axis1)
        self.axis2.set(axis2)
        self.axis3.set(axis3)
        self.axis4.set(axis4)
        self.time.set(time)

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

        self.timeBox.delete(0, tk.END)
        self.timeBox.insert(0, str(int(self.timeVal.get())))
        
        self.a.updateImage(int(self.axis1Val.get()),int(self.axis1Val.get()) + int(self.axis2Val.get()),int(self.axis1Val.get()) + int(self.axis2Val.get()) + int(self.axis3Val.get()))
        self.b.updateImage(int(self.axis0Val.get()))
        self.c.updateImage(int(self.axis4Val.get()))
        # int(self.axis1Val.get()) + int(self.axis2Val.get()) + int(self.axis3Val.get())

    def directionSelection(self):
        return self.radioChoice.get()  

    def getIntArray(self):
        value = tk.StringVar()
        value = self.saveValueBox.get('{}.{}'.format(self.position,0), '{}.{}{}'.format(self.position+1,0,"-1c"))
        tempArray = tk.StringVar()
        intArray = [0, 0, 0, 0, 0, 0]
        counter = 0
        for number in value: 
            if number == "(":
                continue
        
            if number == "," or number == ")":
                
                intArray[counter] = int(tempArray.get())
                
                print(intArray)    
                tempArray.set("")
                counter = counter + 1 
                continue
            
            tempArray.set(tempArray.get() + number)
        return intArray          

    def sendCommand(self): 
        if self.loadAllFlag.get() == True:
            pass
            # Send multiple Commands: 
            # counter = 0
            # while(counter != self.numberOfEntries):
                
            #     counter = counter + 1
            #     self.moveSelector(-1)
            # self.loadAllFlag.set(False)
            # self.moveSelector(self.numberOfEntries)
        else:
            pass

    def run(self):
        self.root.mainloop()        



a = gui()

a.run()

