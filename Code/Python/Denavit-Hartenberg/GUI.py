# import tkinter as tk


# class GUI(): 
#     def __init__(self): 
#         self.width = 500 
#         self.height = 250 
#         self.connected = False
#         self.connectButton = None
#         self.circle = None
#         self.setup()

#     def setup(self):
#         self.root = tk.Tk()
#         self.root.title("Robotic Arm")
#         self.root.geometry(str(self.width) + "x" + str(self.height)) # Sets the geometry of the window
#         self.root.protocol("WM_DELETE_WINDOW", self.on_closing) # Close the session if window closed

#         self.connectToDevice()

#     def connectToDevice(self):
#         connectedFrame = tk.Frame(self.root, highlightbackground="black", highlightthickness = 1)
#         connectedFrame.pack()   

#         self.circle = tk.Canvas(connectedFrame, bg="blue", height=30, width=30)
#         self.circle.create_oval(4,4,20,20,outline="black", fill="green", width=2)
#         self.circle.pack(side = "left")    

#         self.connectButton = tk.Button(connectedFrame, text = "Connect", command = self.connectButtonPressed)
#         self.connectButton.pack()

#     def connectButtonPressed(self):
#         if self.connected == False: 
#             self.connected = True 
#             self.connectButton['text'] = "Disconnect"
#             Canvas.itemconfig(self.circle, fill='red')
            
            
#         else: 
#             self.connected = False
#             self.connectButton['text'] = "Connect"
#             Canvas.itemconfig(self.circle, fill='green')
            
            

#     def run(self): 
#         self.root.mainloop()

#     def on_closing(self):
#         self.root.destroy()


# a = GUI()
# a.run()

# Functions
def on_closing():
    root.destroy()



import tkinter as tk
from tkinter.scrolledtext import ScrolledText

leftColumnWidth = 180 
midColumnWidth = 500
rightColumnWidth = 180

windowWidth = leftColumnWidth + midColumnWidth + rightColumnWidth
windowHeight = 500

root = tk.Tk()
# root.resizable(width=False, height=False)
root.title("Robotic Arm")
root.geometry(str(windowWidth) + "x" + str(windowHeight)) # Sets the geometry of the window
root.protocol("WM_DELETE_WINDOW", on_closing) # Close the session if window closed



#Left Column
leftFrame = tk.Frame(root, width = leftColumnWidth, height = windowHeight)
leftFrame.pack(side='left')

#Right Column
rightFrame = tk.Frame(root, width = rightColumnWidth, height = windowHeight)
rightFrame.pack(side='right')

#Mid Columns
midFrame = tk.Frame(root, width = midColumnWidth, height = windowHeight)
midFrame.pack()



## ConnectFrame: 
connectedFrame = tk.Frame(leftFrame, highlightbackground="black", highlightthickness = 1)
connectedFrame.pack()   

circle = tk.Canvas(connectedFrame, bg="blue", height=15, width=15)
circle.create_oval(6,6,15,15,outline="black", fill="green", width=2)
circle.pack(side = "left")

connectButton = tk.Button(connectedFrame, text = "Connect")
connectButton.pack()

## Sliders 
sliderFrame = tk.Frame(leftFrame,highlightbackground="black", highlightthickness = 1)
sliderFrame.pack()

axis0 = tk.Scale(sliderFrame, from_=-90, to=90, orient=tk.HORIZONTAL, length = 180, label='axis0')
axis0.set(0)
axis0.pack()

axis1 = tk.Scale(sliderFrame, from_=-90, to=90, orient=tk.HORIZONTAL, length = 180, label='axis1')
axis1.set(0)
axis1.pack()

axis2 = tk.Scale(sliderFrame, from_=-90, to=90, orient=tk.HORIZONTAL, length = 180, label='axis2')
axis2.set(0)
axis2.pack()

axis3 = tk.Scale(sliderFrame, from_=-90, to=90, orient=tk.HORIZONTAL, length = 180, label='axis3')
axis3.set(0)
axis3.pack()

saveButton = tk.Button(sliderFrame, text='Save')
saveButton.pack(side='left')
resetButton = tk.Button(sliderFrame, text='Reset')
resetButton.pack(side='right')

# ListBox
listBoxFrame = tk.Frame(leftFrame, highlightbackground="black", highlightthickness = 1)
listBoxFrame.pack()

listBox = tk.Listbox(listBoxFrame, highlightcolor ="black", highlightthickness= 1, height = 12)
listBox.pack()

#AnimationBox 
aniboxFrame = tk.Frame(midFrame, highlightbackground="black", highlightthickness = 2, width =midColumnWidth, height = windowHeight)

aniboxFrame.pack()

#System Messages
sysMessageFrame = tk.Frame(rightFrame, highlightbackground="black", highlightthickness = 1)
sysMessageFrame.pack()

scrolledText = ScrolledText(sysMessageFrame, width = 30, height = 45, font = ("Times New Roman",10))

# scrolledText.grid(column = 0, pady = 10, padx = 10)
scrolledText.insert(tk.INSERT,
"""\
This is a scrolledtext widget to make tkinter text read only.
1
2
3
4
5
6
""")
scrolledText.configure(state ='disabled')

scrolledText.pack()

msg = tk.StringVar()
# sysMessage = tk.Message(sysMessageFrame, textvariable=msg, relief=tk.RIDGE, justify = tk.LEFT, width = rightColumnWidth)
msg.set("a")





root.mainloop()

