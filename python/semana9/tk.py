#importar la librería
from tkinter import *

#Crear el widget tk
root = Tk()
root.title("Titulo del programa")
root.resizable (1,1)

"""
Label(root,text="Hola mundo").pack()
etiqueta = Label (root, text = "Aquí tenemos otra etiqueta")
etiqueta.pack()
etiqueta.config (font=("Verdana",24), bg = "blue", fg = "green")

etiqueta = Label (root, text = "Digite su nombre: ")
etiqueta.pack(side="left")
#etiqueta.config (font=("Verdana",24), bg = "blue", fg = "green")
cuadro= Entry(root)
cuadro.pack(side = "right")
"""
etiqueta = Label (root, text = "Digite su nombre completo: ")
etiqueta.grid(row = "0", column= "0")
#etiqueta.config (font=("Verdana",24), bg = "blue", fg = "green")
cuadro= Entry(root)
cuadro.grid(row = "0", column= "1")

etiqueta = Label (root, text = "Digite su primer apellido: ")
etiqueta.grid(row = "1", column= "0")
#etiqueta.config (font=("Verdana",24), bg = "blue", fg = "green")
cuadro= Entry(root)
cuadro.grid(row = "1", column= "1")

#Siempre colocar abajo de último
root.mainloop()
