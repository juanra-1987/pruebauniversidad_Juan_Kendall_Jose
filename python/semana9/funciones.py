import os
os.system("cls")
#Variables globales.
numero1=100
print(id(numero1))
def sumar():
    #Estas son variables locales
    numero1=20
    print(id(numero1))
    numero2=30
    sumar = numero1 + numero2
    print ("la suma es de:", sumar)

sumar()
print (numero1)
