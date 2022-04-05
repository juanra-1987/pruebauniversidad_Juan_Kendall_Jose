import os
os.system ("cls")

colores = {
    "amarillo":"yellow",
    "verde":"green", 
    "blanco":"white",
    "rojo":"red"
}
for item in colores:
    print ("El color en español es :",item, "El color en ingles es:", colores.get(item))
print ("___________________________________________")
for clave,valor in colores.items():
    print ("En español es: ", clave, "En inlges es: ", valor)
print (type(colores))
