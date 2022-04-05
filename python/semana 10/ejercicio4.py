from tkinter import *


root=Tk()

etiqueta= Label(root)
etiqueta.grid (column=1,row=2)

def presionar():
    txt = txt1.get()
    if txt == "":
        print ("Está Vacío")
    else:
        print ("Tenemos Datos")
        etiqueta.config(text=txt)


root.title("Mi primera etiqueta")
root.geometry("400x400")


Label(root,text="Digite datos:",font=("Arial Bold",20)).grid(column=0,row=0)
txt1 = Entry(root)
txt1.grid(column=1,row=0)

btn1 = Button (root, text="clik aquí",command=presionar).grid (column=1,row=1)



root.mainloop()