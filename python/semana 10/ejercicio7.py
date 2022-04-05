from tkinter import *
 
ventana = Tk()

r1 = Radiobutton (ventana, text= "py", value=1)
r2 = Radiobutton (ventana, text= "java", value=2)
r3 = Radiobutton (ventana, text= "c#", value=3)

r1.grid(column=0,row=0)
r2.grid(column=1,row=0)
r3.grid(column=2,row=0)

ventana.mainloop()