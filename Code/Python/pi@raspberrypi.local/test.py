import tkinter as tk

root = tk.Tk()

def click(key):
    # print the key that was pressed
    print(key.char)
    if(key.char == ""):
        print("Enter!")

entry = tk.Entry()
entry.grid()
# Bind entry to any keypress
entry.bind("<Key>", click)


root.mainloop()