import tkinter as tk
from tkinter import Canvas, DoubleVar, Scale, Widget, mainloop, ttk
from tkinter.constants import ANCHOR

from PIL import Image, ImageTk
import math

class sideView():
    def __init__(self, root, Width, Height, scale = 1):
        self.scale = scale
        self.canvas = tk.Canvas(root, width = Width, height = Height, bg="black")
        self.canvas.grid()
        # self.canvas.grid(row=0,column=0,sticky="nesw")
        # self.canvas.pack()#(expand=tk.YES, fill=tk.BOTH)

        self.x0 = 250
        self.y0 = 350

        self.l1 = self.scale*60
        self.l2 = self.scale*60
        self.l3 = self.scale*136
        self.l4 = self.scale*122
        self.l5 = self.scale*138


        self.armOffset_X = self.scale*50
        self.armOffset_Y = -self.scale*74
        self.axis2Offset = -self.scale*104 + self.armOffset_Y
        self.axis3Offset = -self.scale*242 + self.armOffset_Y
        self.axis4Offset = -self.scale*440 + self.armOffset_Y
        

        

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
            return image.resize((round(self.scale*480),round(self.scale*126))) 
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
        return math.sin(self.toRad(deg))    

    def cos(self, deg):
        return math.cos(self.toRad(deg))  


class topView():
    def __init__(self, root, Width, Height, scale = 1):
        self.scale = scale
        self.canvas = tk.Canvas(root, width = Width, height = Height, bg="black")
        self.canvas.grid()
        # self.canvas.grid(row=0,column=0,sticky="nesw")
        # self.canvas.pack()#(expand=tk.YES, fill=tk.BOTH)

        self.x0 = self.scale*200
        self.y0 = self.scale*230

        self.l1 = self.scale*74
    


        self.armOffset_X = 0
        self.armOffset_Y = -self.scale*110
        
        

        self.loadImages()
        self.base  = self.scaleImage(self.base,0)
        self.axis1 = self.scaleImage(self.axis1,1)

        self.updateImage(0)

        

    def loadImages(self):
        self.base  = Image.open('Images/baseTopView.png')
        self.axis1 = Image.open('Images/ArmTopView.png')

        

    def scaleImage(self, image, axis = None):
        if axis == 0: 
            return image.resize((round(self.scale*246),round(self.scale*274))) 
        elif axis == 1: 
            return image.resize((round(self.scale*84),round(self.scale*222))) 
        else:
            return "Error"

        

    def createTkImage(self, image):
        return ImageTk.PhotoImage(image)

    def rotateImage(self, image, rotation):
        return image.rotate(rotation, expand = tk.TRUE)   

    def createImage(self, x, y, Image):
        return self.canvas.create_image(x, y, image = Image)

    def updateImage(self, Angle1):    
        self.baseTK = self.createTkImage(self.base)
        self.createImage(self.x0, self.y0, self.baseTK)

        self.axis1TK = self.createTkImage(self.rotateImage(self.axis1, Angle1))
        self.createImage(self.x0 - self.l1*self.sin(Angle1), self.y0 + self.armOffset_Y + self.l1*(1-self.cos(Angle1)), self.axis1TK)

        # self.create_circle(self.x0, self.y0 + self.armOffset_Y, 10, self.canvas)
        # self.create_circle(self.x0, self.y0 + self.armOffset_Y + 74, 10, self.canvas)
        
        
    def toRad(self, deg):
        return deg*math.pi/180    

    def sin(self, deg):
        return math.sin(self.toRad(deg))    

    def cos(self, deg):
        return math.cos(self.toRad(deg))  

    def create_circle(self, x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)    


class frontView():
    def __init__(self, root, Width, Height, scale = 1):
        self.scale = scale
        self.canvas = tk.Canvas(root, width = Width, height = Height, bg="black")
        self.canvas.grid()
        # self.canvas.grid(row=0,column=0,sticky="nesw")
        # self.canvas.pack()#(expand=tk.YES, fill=tk.BOTH)

        self.x0 = 100# self.scale*200
        self.y0 = 95#self.scale*230

        self.l1 = self.scale*74
    


        self.armOffset_X = 100
        self.armOffset_Y = 95#-self.scale*180
        
        

        self.loadImages()
        self.front  = self.scaleImage(self.front,0)
        

        self.updateImage(0)

        

    def loadImages(self):
        self.front  = Image.open('Images/EndEffectorFront.png')
        

        

    def scaleImage(self, image, axis = None):
        if axis == 0: 
            return image.resize((round(self.scale*454),round(self.scale*450))) 
        else:
            return "Error"

        

    def createTkImage(self, image):
        return ImageTk.PhotoImage(image)

    def rotateImage(self, image, rotation):
        return image.rotate(rotation, expand = tk.TRUE)   

    def createImage(self, x, y, Image):
        return self.canvas.create_image(x, y, image = Image)

    def updateImage(self, Angle1):    
        self.frontTK = self.createTkImage(self.rotateImage(self.front, Angle1))
        self.createImage(self.x0, self.y0, self.frontTK)

        

        # self.create_circle(self.x0, self.y0 + self.armOffset_Y, 10, self.canvas)
        # self.create_circle(self.x0, self.y0 + self.armOffset_Y + 74, 10, self.canvas)
        
        
    def toRad(self, deg):
        return deg*math.pi/180    

    def sin(self, deg):
        return math.sin(self.toRad(deg))    

    def cos(self, deg):
        return math.cos(self.toRad(deg))  

    def create_circle(self, x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)    

# root = tk.Tk()
# root.geometry("550x380")

# a = frontView(root, 400, 380, 1)
# a.updateImage(-0)

# root.mainloop()