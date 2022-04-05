import os
os.system("cls")

"""
Realizar un programa en python que cree una lista y esta la inicialízala con 5 cadenas de caracteres leídas por teclado y estos deben de ser mostrados
"""
lista = []
for i in range (5):
    a= input(str(f"Digite la cadena de caracteres número {i+1}: "))
    lista.append(a)
    
print (lista)