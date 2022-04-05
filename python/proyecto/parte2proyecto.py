from tkinter import * 
from tkinter.ttk import *

ventana2 = Tk() 
ventana2.geometry("200x200") 

def ventanamenu1(): 
    nuevaVentanmenu1 = Toplevel(ventana2)
    nuevaVentanmenu1.title("Menú 1: Conocer el precio de compra o venta animales de producción.") 
    nuevaVentanmenu1.geometry("200x200") 
    Label(nuevaVentanmenu1,text ="Ya estamos en una nueva ventana").grid(column=0,row=1)

btn = Button(ventana2,text ="Siguiente",command = ventanamenu1) 
btn.grid(column=0,row=3) 

mainloop() 
