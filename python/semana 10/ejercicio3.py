from pickletools import TAKEN_FROM_ARGUMENT8U
from tkinter import *


root=Tk()
root.title("Mi primera etiqueta")
root.geometry("300x400")

bt=Button(root,text="ojo")
bt.pack()

Button(root,text="Este es otro botón").pack()

root.mainloop()
