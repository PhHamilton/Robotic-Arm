import tkinter as tk
from tkinter import Canvas, DoubleVar, Scale, Widget, mainloop, ttk
from tkinter.constants import ANCHOR

# Screen res: 1280 x 720

class gui():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.initGui()
        self.createMainFrames()

    def initGui(self):
        self.root = tk.Tk()
        
        self.padding = 5
        self.root.geometry('{}x{}'.format(self.width, self.height))
        self.root.title("Robotic Arm GUI")

    def createMainFrames(self):
        self.motionFrame = ttk.LabelFrame(self.root, text = "Robot Motion")    
        self.motionFrame.grid(row=0,column=0, sticky = "nesw")

        self.storedValueFrame = ttk.LabelFrame(self.root, text = "Store Values")    
        self.storedValueFrame.grid(row=1,column=0, sticky = "nesw")

    def run(self):
        self.root.mainloop()


a = gui()
a.run()