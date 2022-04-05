from tkinter import *


ventana=Tk()
ventana.title("Mi primera etiqueta")
ventana.geometry("400x400")


txt1 = Entry(ventana)
txt1.pack()
txt2 = Entry(ventana)
txt2.pack()

etiqueta=Label(ventana)
etiqueta.pack()


def sumar ():
    numero1=int(txt1.get())
    numero2=int(txt2.get())
    print (type(numero1),type(numero2))
    resultado= numero1+numero2
    etiqueta.config(text=resultado)



btn = Button(ventana,text="Precionar",command=sumar)
btn.pack()



ventana.mainloop()