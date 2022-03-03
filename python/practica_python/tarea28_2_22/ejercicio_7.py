import os
os.system ("cls")

print("Digite dos números")
dato1=input("Digite el primer número:  ")
dato2=input("Digite el segundo número:  ")
a=(dato1.isdigit())
b=(dato2.isdigit())


if a== True and b== True:
    if dato1==dato2:
        print("Ambos números son iguales")
    elif dato1 != dato2:
        print("Los datos digitados son distintos")
        if dato1 > dato2:
            print(f"El primer dato es mayor que {dato2}")
        elif dato1 <= dato2:
            print(f"El segundo número es igual o mayor que {dato1}")
else:
    print ("Alguno o ambos de los datos ingresados no es un dato numérico")