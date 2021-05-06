import tkinter as tk


class SliderAndValue():
    def __init__(self): 
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.slider = tk.Scale(self.root, from_=-90, to=90, orient=tk.HORIZONTAL, length = 180)
        self.slider.set(0)
        self.slider.pack()

        self.button = tk.Button(self.root, text='Save', command = self.saveValue)
        self.button.pack()


        self.text = tk.StringVar()

    def on_closing(self):
        self.root.destroy()

    def saveValue(self):
        self.text = self.slider.get()

    def run(self):
        self.root.mainloop()


a = SliderAndValue()
a.run()










