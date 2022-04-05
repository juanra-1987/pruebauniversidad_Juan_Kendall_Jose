import os
os.system("cls")


#Diccionarios
#Como se accede en las listas [] -> Indice!!!!, en una tupla -> indice
#Como se acceden a los diccionarios -> Clave , key
lista =[]
tupla = ()
diccionario = {"uno" : 1, "dos" : 2}

print (diccionario)

#par acceder a las claves

print (diccionario["dos"])

print (diccionario.keys())

print (diccionario.values())

diccionario["tres"] = 3

print (diccionario)

diccionario["tres"] = 10

print (diccionario)

lista.append(100)

print (lista)

valor = "dos"

print (valor in diccionario)

valor = "cien"

print (valor in diccionario)

for i in diccionario:
    print (i)

for i in diccionario.values():
    print (i)

for clave,valor in diccionario.items():
    print (clave,"->",valor)