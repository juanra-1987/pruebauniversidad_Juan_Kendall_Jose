import os
os.system ("cls")

print ("Imprime los años comprendidos entre dos años que el usuario digite:")
anno1=int(input("Año 1: "))
anno2=int(input("Año 2: "))
anno=0
print (f"Los años comprendidos entre el año {anno1} y el año {anno2} son:")
if anno1<anno2:
    for anno in range (anno1+1,anno2,1):
        print("Año ",anno)
else:
    print (f"El segundo año debe ser mayor a {anno1}")
