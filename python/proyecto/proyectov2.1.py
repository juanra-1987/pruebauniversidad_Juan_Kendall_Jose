from msilib.schema import ComboBox
import os
from tkinter import font

from setuptools import Command

#from proyecto.parte2proyecto import ventanamenu1
os.system("cls")

from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk


ventanaMenu1=tk.Tk()
ventanaMenu1.title("Menú 1")
ventanaMenu1.geometry("950x350")
texto= StringVar()
texto.set("Según los registros de compra y venta de animales del tipo: ")
texto2= StringVar()
texto2.set("Según los registros de compra y venta en el mes de: ")

def obtener():
    
    if combo.get() == "Bovinos":
        texto.set("Según los registros de compra y venta de animales del tipo: Bovinos ")
    if combo.get() == "Ovinos":
        texto.set("Según los registros de compra y venta de animales del tipo: Ovino ")
    if combo.get() == "Porcinos":
        texto.set("Según los registros de compra y venta de animales del tipo: Porcino")

def obtener2():        
    if combo2.get() == "Enero":
        texto.set("Según los registros de compra y venta en el mes de: Enero")
    if combo2.get() == "Febrero":
        texto.set("Según los registros de compra y venta en el mes de: Febrero")
    if combo2.get() == "Marzo":
        texto.set("Según los registros de compra y venta en el mes de: Marzo")
    if combo2.get() == "Abril":
        texto.set("Según los registros de compra y venta en el mes de: Abril")
    if combo2.get() == "Mayo":
        texto.set("Según los registros de compra y venta en el mes de: Mayo")
    if combo2.get() == "Junio":
        texto.set("Según los registros de compra y venta en el mes de: Junio")
    if combo2.get() == "Julio":
        texto.set("Según los registros de compra y venta en el mes de: Julio")
    if combo2.get() == "Agosto":
        texto.set("Según los registros de compra y venta en el mes de: Agosto")
    if combo2.get() == "Setiembre":
        texto.set("Según los registros de compra y venta en el mes de: Setiembre")
    if combo2.get() == "Octubre":
        texto.set("Según los registros de compra y venta en el mes de: Octubre")
    if combo2.get() == "Noviembre":
        texto.set("Según los registros de compra y venta en el mes de: Noviembre")
    if combo2.get() == "Diciembre":
        texto.set("Según los registros de compra y venta en el mes de: Diciembre")

preciosbovinosmes= {"Enero":1000,"Febrero":1200,"Marzo":1300,"Abril":1400,"Mayo":1500,"Junio":1600,"Julio":1700,"Agosto":1800,"Septiembre":1900,"Octubre":2000,"Noviembre":2100, "Diciembre":2200}
preciosovinosmes= {"Enero":2000,"Febrero":2200,"Marzo":2300,"Abril":2400,"Mayo":2500,"Junio":2600,"Julio":2700,"Agosto":2800,"Septiembre":2900,"Octubre":3000,"Noviembre":3100, "Diciembre":3200}
preciosporcinosmes= {"Enero":3000,"Febrero":3200,"Marzo":3300,"Abril":3400,"Mayo":3500,"Junio":3600,"Julio":3700,"Agosto":3800,"Septiembre":3900,"Octubre":4000,"Noviembre":4100, "Diciembre":4200}


lbl2Mensaje = tk.Label(ventanaMenu1,text ="Elija uno de los tres animales de producción a consultar:",font=("Arial Bold",16))
lbl2Mensaje.grid(column=0,row=3)

combo=ttk.Combobox(ventanaMenu1,state="readonly",values=["Bovinos", "Ovinos", "Porcinos"])
combo.current(0)
combo.grid (column=1,row=3)

lbl3Mensaje = tk.Label(ventanaMenu1,text ="Elija el mes en el cuál desea realizar la consulta:",font=("Arial Bold",16))
lbl3Mensaje.grid(column=0,row=4)

combo2=ttk.Combobox(ventanaMenu1,state="readonly",values=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre", "Diciembre"])
combo2.current(0)
combo2.grid (column=1,row=4)

boton = Button(ventanaMenu1, command=obtener, text="Obtener")
boton.grid (column=2,row=3)

boton2 = Button(ventanaMenu1, command=obtener2, text="Obtener")
boton2.grid (column=2,row=4)


etiqueta1 = tk.Label(ventanaMenu1,textvariable=texto,font=("Arial Bold",12))
etiqueta1.grid(column=0,row=7)

etiqueta2 = tk.Label(ventanaMenu1,textvariable=texto2,font=("Arial Bold",12))
etiqueta2.grid(column=0,row=8)


# tk.Label(ventanaMenu1,text="Según los registros de compra y venta de animales get.combox, para el\n mes de combox.meses, el precio por kilogramo de peso vivo es \nde xx colones",font=("Arial Bold",14),fg="white",bg="blue").grid(column=0,row=6)


""""
Según los registros de compra y venta de animales get.combox, para el mes de combox.meses, el precio por kilogramo de peso vivo esde xx colones
"""

ventanaMenu1.mainloop()