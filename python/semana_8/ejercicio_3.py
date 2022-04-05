import os

os.system ("cls")

lista = [20,65,12,2,8,65,48,1,5,8]
pares =[]
impares = []

for i in lista:
    operacion = i%2
    if operacion == 0:
        pares.append(i)
    else:
        impares.append(i)    

print ("La lista de números pares es: ", pares)
print ("La lista de números impares es: ", impares)