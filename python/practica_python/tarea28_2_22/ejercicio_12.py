import os
os.system ("cls")

print ("Digite una palabra para determinar si es un Palíndromo o no")
palabra=input().upper()

if palabra.isalpha() == True:
    
    if palabra[::-1] ==  palabra[::1]:
        print ("La palbra digitada cumple con las características de un Palíndromo")
    else:
        print ("La palbra digitada NO cumple con las características de un Palíndromo")    
else:
     print ("La cadena de carateres ingresada no corresponde a una palabra, ya que contiene espacios o datos númericos.")