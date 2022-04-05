import os
os.system("cls")

"""
Realizar un programa en python que lea por teclado las 5 notas obtenidas por un usuario (comprendidas entre 1 y 100). A continuación, debe mostrar todas las notas, y el promedio de las notas ingresadas.
"""

notas = []

for i in range (5):
    a = input(f"Digite la nota {i+1} (entre 1 y 100): ")
    notas.append(a)

print (notas)

suma=0

for j in range (len(notas)):
    print (f"La nota {j+1} es de:",notas[j])
    suma = int(notas[j]) +suma
    
promedio=suma/len(notas)
print ("El promedio de las notas es de:  ", promedio)