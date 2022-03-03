import os
os.system ("cls")

print ("Ingrese tres notas para obtener el promedio ponderado")
nota1 = float(input("Ingrese la primera nota:\n "))
nota2 = float(input("Ingreses las segunda nota: \n "))
nota3 = float(input("Ingreses la tercera nota:\n "))

promedio= (nota1+nota2+nota3)/3

print ("El promedio de la tres notas es: ", promedio) 
