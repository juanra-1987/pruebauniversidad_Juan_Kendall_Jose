import os
#from re import A
os.system ("cls")

def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
for i in [1,2,3,4,5,6,7,8,9,10]:
    print ("Cálculo de costo de la entrada según edad")
    edad=input ("Digite la edad del cliente (en números):\n")
    if es_numerico (edad) == True:
        edad=int(edad)
        if edad>0 and edad < 100:
            if edad<4:
                print ("Por ser menor de 4 años, entra GRATIS")
                break
            elif edad>4 and edad< 18:
                print("Debe cancelar un monto de 5 Dólares")
                break
            else:
                print ("El monto de la entrada para su edad es 10 Dólares")   
                break 
        else:
            print("Verifique el dato ingresado")
    else:
        print ("El dato digitado no corresponde a un número valido")
        print (f"\tIntento {i} de 10")

