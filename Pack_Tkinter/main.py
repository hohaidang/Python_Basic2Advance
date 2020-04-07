
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

buttonframe = Frame(root)
buttonframe.pack(side = BOTTOM)

redbutton = Button(frame, text="red", fg="red")
redbutton.pack(side = LEFT)

blackbutton = Button(buttonframe, text="Black", fg='black')
blackbutton.pack(side = BOTTOM)

var = IntVar()
c = Checkbutton(root, text="Fck", variable = var)
c.pack(side = BOTTOM)

root.mainloop()


print("Hello World")