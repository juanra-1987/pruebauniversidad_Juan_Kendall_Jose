import os
os.system ("cls")

personas=[]


cantNombres=int(input("Digite la cantidad de nombre que desea digitar: "))

# for i in range (0,cantNombres) :
#     listaNombres.append(input (f"Nombre # {i}"))

# for i in listaNombres:
#     print (i)

for item in range (0,cantNombres) :
    nombre = input ("digite el nombre ")
    edad = input ("digite la edad ")
    #asignar una lista
    p = [nombre,edad]
    #2da forma
    # p= []
    # p.append(nombre)
    # p.append(edad)
    personas.append(p)

    #print (personas) 
for i in p:
        print (i)
    