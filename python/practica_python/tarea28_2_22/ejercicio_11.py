from ast import AsyncFunctionDef
from distutils.command.clean import clean
import os
os.system ("cls")

def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

print("Por favor digite una letra del teclado, para determinar si es una VOCAL")

i=0

while i<3:
    
    letra=input("Digite su elección:\n ").upper()
    a=es_numerico(letra)
    if len(letra) <=1:
        
        if letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
            print("Usted a digitado una Vocal")
            break
        elif a == True:
            print("Debe digitar solamente letras y no números")
            i=i+1
            if i == 2:
                print ("Última oportunidad")
                clean
        else:
            print ("La letra digitada no es una Vocal")  
            break  
    else:
        print("Solo debe digitar un caracter")
        i=i+1
        if i == 2:
            print ("Última oportunidad")
            clean
