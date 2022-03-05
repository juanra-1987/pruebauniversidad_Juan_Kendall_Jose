from ast import AsyncFunctionDef
import os
os.system ("cls")


print("Digite dos palabras")
palabra1=str(input("Digite la priemera palabra:  "))
palabra2=str(input("Digite la segunda palabra:  "))
palabra1=palabra1.upper()
palabra2=palabra2.upper()


if (palabra1[-3:]) ==(palabra2[-3:]):
    print ("Las plabras escritas RIMAN")
elif (palabra1[-2:]) ==(palabra2[-2:]):
    print ("Las plabras escritas RIMAN UN POCO")
else:
    print ("Las palabras escritas NO RIMAN")
