
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

# class app():
#     def __init__(self, root, Width, Height, scale):
#         self.scale = scale
#         self.canvas = tk.Canvas(root, width = Width, height = Height, bg="black")
#         self.canvas.grid()
#         # self.canvas.grid(row=0,column=0,sticky="nesw")
#         # self.canvas.pack()#(expand=tk.YES, fill=tk.BOTH)

#         self.x0 = 500
#         self.y0 = 680

#         self.l1 = 60
#         self.l2 = 60
#         self.l3 = 136
#         self.l4 = 121
#         self.l5 = 138


#         self.armOffset_X = 50
#         self.armOffset_Y = -75
#         self.axis2Offset = -105 + self.armOffset_Y
#         self.axis3Offset = -242 + self.armOffset_Y
#         self.axis4Offset = -441 + self.armOffset_Y
        

        

#         # raw_image = Image.open('Images/Axis1.png')
#         # raw_image = raw_image.resize((172,157))
#         # self.my_img = ImageTk.PhotoImage(raw_image)
#         # self.canvas.create_image(self.x0, self.y0, image=self.my_img)
#         self.loadImages()
#         self.base  = self.scaleImage(self.base,0)
#         self.axis1 = self.scaleImage(self.axis1,1)
#         self.axis2 = self.scaleImage(self.axis2,2)
#         self.axis3 = self.scaleImage(self.axis3,3)
#         self.axis4 = self.scaleImage(self.axis4,4)
    
        
#         self.updateImage(0, 0, 0)

        

#     def loadImages(self):
#         self.base  = Image.open('Images/Base.png')
#         self.axis1 = Image.open('Images/Axis1.png')
#         self.axis2 = Image.open('Images/Axis2.png')
#         self.axis3 = Image.open('Images/Axis3.png')
#         self.axis4 = Image.open('Images/Axis4AndEndeffector.png')
        

#     def scaleImage(self, image, axis = None):
#         if axis == 0: 
#             return image.resize((round(self.scale*481),round(self.scale*127))) 
#         elif axis == 1: 
#             return image.resize((round(self.scale*142),round(self.scale*126))) 
#         elif axis == 2 or axis == 3:
#             return image.resize((round(self.scale*142),round(self.scale*188)))
#         elif axis == 4: 
#             return image.resize((round(self.scale*142),round(self.scale*316)))
#         elif axis == 5:
#             return image.resize((round(self.scale*142),round(self.scale*148)))
#         else:
#             return "Error"

        

#     def createTkImage(self, image):
#         return ImageTk.PhotoImage(image)

#     def rotateImage(self, image, rotation):
#         return image.rotate(rotation, expand = tk.TRUE)   

#     def createImage(self, x, y, Image):
#         return self.canvas.create_image(x, y, image = Image)

#     def updateImage(self, Angle1, Angle2, Angle3):    
#         self.baseTK = self.createTkImage(self.base)
#         self.createImage(self.x0, self.y0, self.baseTK)

#         self.axis1TK = self.createTkImage(self.rotateImage(self.axis1, 0))
        
        
#         self.axis2TK = self.createTkImage(self.rotateImage(self.axis2, Angle1))
#         self.createImage(self.x0 + self.armOffset_X -self.l1*self.sin(Angle1), self.y0 + self.axis2Offset + self.l1*(1-self.cos(Angle1)), self.axis2TK)

#         self.createImage(self.x0 + self.armOffset_X,self.y0 + self.armOffset_Y, self.axis1TK)

#         self.axis3TK = self.createTkImage(self.rotateImage(self.axis3, Angle2))
#         self.createImage(self.x0 + self.armOffset_X-(self.l2+self.l3-self.l1)*self.sin(Angle1)-self.l2*self.sin(Angle2), self.y0 + self.axis3Offset +(self.l2+self.l3-self.l1)*(1-self.cos(Angle1)) + self.l2*(1-self.cos(Angle2)), self.axis3TK)

#         self.axis4TK = self.createTkImage(self.rotateImage(self.axis4, Angle3))
#         self.createImage(self.x0 + self.armOffset_X-(self.l2+self.l3-self.l1)*self.sin(Angle1) -self.l5*self.sin(Angle2) -self.l4*self.sin(Angle3),self.y0 + self.axis4Offset +(self.l2+self.l3-self.l1)*(1-self.cos(Angle1)) + self.l5*(1-self.cos(Angle2))+self.l4*(1-self.cos(Angle3)), self.axis4TK)

        

        

#     def toRad(self, deg):
#         return deg*math.pi/180    

#     def sin(self, deg):
#         return math.sin(toRad(deg))    

#     def cos(self, deg):
#         return math.cos(toRad(deg))    

# root = tk.Tk()
# root.geometry("1200x800")

# a = app(root, 1200, 800, 1)
# a.updateImage(30,0,0)

# root.mainloop()