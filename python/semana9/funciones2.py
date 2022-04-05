import os
from tkinter.ttk import setup_master
os.system("cls")


def sumar():
    n1=2
    n2=5
    suma = n1 + n2
    return suma,n1,n2

valorSuma,N1,N2 = sumar ()
print (valorSuma)