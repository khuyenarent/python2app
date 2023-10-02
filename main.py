import random
import tkinter

hello = ["Xin chào! gf g fg f gf gf gf g fg f gf g fg f gf g fg f g", "Hellogfgf gf g fg fg f gf g fg fg", "新潮 fd f df df d fd f df", "シンチャオ d f d df df df"]
number = random.randrange(0,3)
window = tkinter.Tk()
window.geometry('700x200')
window.title("Hello world")
tkinter.Label(window, text=hello[number], font="Helvetica 16 bold").pack()

window.mainloop()