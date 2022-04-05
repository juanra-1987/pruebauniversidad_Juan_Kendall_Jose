import os
os.system ("cls")

agenda ={}
opcion= True

while opcion:
    nombre=input()
    respuesta = input ("salir (s/n)")
    if respuesta.upper() == "S":
        opcion = False
