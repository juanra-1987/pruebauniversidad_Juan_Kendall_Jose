import os

os.system ("cls")

estudiante = []

for item in range (0,5):
    nombre =input ("Por favor digite un nombre: ")
    estudiante.append(nombre)

for i in estudiante:
    print ("El nombre del estudiante es: ",i)


print (type(estudiante))