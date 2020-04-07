
from tkinter import *

# root = Tk()
# frame = Frame(root)
# frame.pack()
# 
# buttonframe = Frame(root)
# buttonframe.pack(side = BOTTOM)
# 
# redbutton = Button(frame, text="red", fg="red")
# redbutton.pack(side = LEFT)
# 
# blackbutton = Button(buttonframe, text="Black", fg='black')
# blackbutton.pack(side = BOTTOM)
# 
# k = False
# # k = ~k
# print(k)
# def did_tap_run():
#     print("a")
# 
# var = IntVar()
# c = Checkbutton(root, text="Fck", variable = var, command=did_tap_run)
# c.pack(side = BOTTOM)
# 
# root.mainloop()
# print(var._default)
# 
# print("Hello World")

import tkinter as tk
 

window = tk.Tk()
window.title('My Window')
window.geometry('100x100')
 
l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()
 
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not anything')
    else:
        l.config(text='I love both')
 
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
 
window.mainloop()

print("var1", var1)
print("var2", var2)
print("c1", c1)
print("c2", c2)