from tkinter import *

root = Tk()
root.geometry("500x500")

# Create label widget
myLabel = Label(root, text="Hello World!")
# Pack it onto the screen.
myLabel.pack()

root.mainloop()