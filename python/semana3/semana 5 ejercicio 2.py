nombre=str
edad=int

print("Digite su nombre:\n" ),input(nombre)
print("Digite su edad:\n" ),input(edad)
#print (type(nombre))
#print (type(nombre))
print("Su nombre es", nombre, "y su edad es: ",edad)

if type(nombre) ==str:
    print("ES UNA CADENA DE CARTACTERES")
else:
    print("No es una cadena de caracteres")
    nombre=""

if type(edad)==int:
    print("Es un entero")
else:
    print("omg")
