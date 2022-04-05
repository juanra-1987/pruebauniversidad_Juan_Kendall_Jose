import os
os.system("cls")

peliculas ={}

print ("bienvenido al cineclub")

print ("Digite la película y el genero que desee guardar en el inventario")
for item in range (4):
    pelicula = input ("película : ")
    genero = input ("genero: ")
    peliculas [pelicula] = genero

for i,j in peliculas.items():
    print("la pelicula: ",i," es de genero: ",j)

