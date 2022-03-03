#Condicionales if, según, elif
#else if es elif
#string str
#integer int
#ciclos While, for
#para limpiar pantalla de la consola, librerias, clases, apis   import os--> interactua con sistema operativo
#Formula random, para 
#para windows cls para limpiar pantalla
import os
os.system ("cls")
#par limpiar
edad = int(input("Digite la edad \n"))

if edad >= 18 and edad < 65:
    print ("Mayor de edad")
elif edad >= 65:
    print ("Es un usted un ciudadano de ORO")
else:   
    print ("Menor de edad")   