import os
os.system ("cls")


print("Realiza el promedio de las notas que el usuario ingrese")

nota1=0
for i in range(1,100):
    nota = float(input(f"Ingrese la nota {i} del estudiante:\t"))
    eleccion=input ("Digite si, si requiere ingresar más notas de lo contrario digite no:\t")
    eleccion1 = eleccion.upper()
    if eleccion1 == "NO" or eleccion1 == "NÓ": 
        nota1=nota+nota1
        break
    nota1=nota+nota1
print (f"El promedio de notas es {nota1/i}")