from tkinter import *

ventana= Tk()

menu1= Menu(ventana)

ventana.config(menu=menu1)

archivoMenu = Menu(menu1)
editarMenu = Menu(menu1)

menu1.add_cascade(label="Editar", menu=editarMenu)
menu1.add_cascade(label="Archivo", menu=archivoMenu)


def salir ():
    ventana.destroy()

editarMenu.add_command(label="Copiar")

archivoMenu.add_command(label="Nueva Ventana")
archivoMenu.add_command(label="Gurdar")
archivoMenu.add_command(label="Salir",command=salir)




ventana.mainloop()
