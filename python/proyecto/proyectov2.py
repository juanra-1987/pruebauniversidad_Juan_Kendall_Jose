import os
from tkinter import font

#from proyecto.parte2proyecto import ventanamenu1
os.system("cls")

from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk

ventana=tk.Tk()
ventana.title("AppPecuario: Amigos del Campo")
ventana.geometry("950x350")

tk.Label(ventana,text="***********************  Bienvenido Productor Pecuario  ***********************\nEn nuestra base de datos hasta el momento podemos trabajar para:\nGanado Bovino, Ovino y Porcino",font=("Arial Bold",22),bg="green").grid(column=0,row=0)

tk.Label(ventana,text="Por favor elija una de las siguientes opciones:",font=("Arial Bold",19),fg="white",bg="blue").grid(column=0,row=1)

seleccion = tk.IntVar()

def btsiguiente():
    if seleccion.get() == 1:
        mensaje = "Has seleccionado: Conocer el precio de compra o venta animales de producción "
    if seleccion.get() == 2:
        mensaje = "Has seleccionado: Conocer el peso estimado de sus animales a partir de sus dimensiones y edades. "
    if seleccion.get() == 3:
        mensaje = "Has seleccionado: Creadores del Proyecto "
    if seleccion.get() == 4:
            mensaje = "Has seleccionado: Salir "
    
    lblMensaje.config(text = mensaje)

r1 = tk.Radiobutton (ventana, text= "1.Conocer el precio de compra o venta animales de producción.",font=("Arial Bold",14),variable= seleccion, value=1,command=btsiguiente)
r2 = tk.Radiobutton (ventana, text= "2.Conocer el peso estimado de sus animales a partir de sus dimensiones y edades.",font=("Arial Bold",14),variable= seleccion, value=2,command=btsiguiente)
r3 = tk.Radiobutton (ventana, text= "3.Creadores del Proyecto",font=("Arial Bold",14),variable= seleccion, value=3,command=btsiguiente)
r4 = tk.Radiobutton (ventana, text= "4.Salir",font=("Arial Bold",14),variable= seleccion, value=4,command=btsiguiente)

r1.grid(column=0,row=2)
r2.grid(column=0,row=3)
r3.grid(column=0,row=4)
r4.grid(column=0,row=5)

lblMensaje = tk.Label(ventana,font=("Arial Bold",12))
lblMensaje.grid(column=0,row=9)





def ventanamenu1(): 
    nuevaVentanmenu1 = Toplevel(ventana)
    nuevaVentanmenu1.title("Menú 1: Conocer el precio de compra o venta animales de producción.") 
    nuevaVentanmenu1.geometry("950x350") 


    Label(nuevaVentanmenu1,text ="Ya estamos en una nueva ventana 1").grid(column=0,row=1)

def ventanamenu2(): 
    nuevaVentanmenu2 = Toplevel(ventana)
    nuevaVentanmenu2.title("Menú 2: Conocer el peso estimado de sus animales a partir de sus dimensiones y edades.") 
    nuevaVentanmenu2.geometry("950x350") 
    Label(nuevaVentanmenu2,text ="Ya estamos en una nueva ventana 2").grid(column=0,row=1)

def ventanamenu3(): 
    nuevaVetanamenu3 = Toplevel(ventana)
    nuevaVetanamenu3.title("Menú 2: Conocer los creadores de la aplicación.") 
    nuevaVetanamenu3.geometry("950x350")
    messagebox("Ing. Juan Rafael Astúa Agüero\nIng.Kendall Andrés León Salazar\nJose Antonio Jiménez Fernández")

def ventanamenu4(): 
    nuevaVetanamenu4 = Toplevel(ventana)
    nuevaVetanamenu4.title("Menú 2: Salir.") 
    nuevaVetanamenu4.geometry("950x350")
    messagebox("Hasta la próxima")

bt1=Button(ventana,text="Siguiente", font= ("Arial Bold",14), command=ventanamenu1)
bt1.grid (column=0,row=8)




ventana.mainloop()

