import os
os.system ("cls")

def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

print("Digite dos números")
dato1=input("Digite el primer número:  ")
dato2=input("Digite el segundo número:  ")

a=es_numerico(dato1)
b=es_numerico(dato2)

if a== True and b== True:
    print("Elija una de las tres opciones\nA) Sumarlos \nB) Restarlos\nC) Multiplicarlos")
    eleccion=str(input())
    eleccion=eleccion.lower()
    dato1=float(dato1)
    dato2=float(dato2)


    if eleccion=="a" or eleccion=="suma" or eleccion=="sumarlos" or eleccion=="sumar":
        suma=dato1+dato2
        print("La suma de ambos número es: ", suma)
    elif eleccion=="b" or eleccion=="resta" or eleccion=="restarlos" or eleccion=="restar":
        resta=dato1-dato2
        print("La resta de ambos número es: ", resta)
    elif eleccion=="c" or eleccion=="multiplica" or eleccion=="multiplicarlos" or eleccion=="multiplicar":
        multiplica=dato1*dato2
        print("El resultado de multiplicar ambos número es: ", multiplica)
    else:
        print("No escogio una opción viable")
else:
    print ("Alguno o ambos de los datos ingresados no es un dato numérico")