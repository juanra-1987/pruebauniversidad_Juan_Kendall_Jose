from cmath import log
import os
import string
os.system ("cls")

print ("Introduzca una cadena de texto, para determinar si la cantidad de caracteres esta en el rango de 3 a 12 caracteres")

cadena = str(input("Digite la cadena de carcacteres a analizar:\n "))
A = True
B = False

if len(cadena) >=3 and len(cadena) <=12:
    print(A)
else:
    print(B)
