# encoding=utf8
from tkinter import *
root = Tk()
textlabel = Label(root, text = 'NOT 18')
textlabel.pack()
photo = PhotoImage(file = '18.gif')
Label(root, image=photo)
mainloop()