import os
os.system ("cls")

def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
def es_numerico2(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

print ("Digite la cantidad de números que desea introducir, para luego clasificarlos en negativos o positivos")
cantidad=input("Cantidad: ")
i=0
contadornegativos=0
contadorpositivos=0

if es_numerico2(cantidad) == True:
    cantidad=int(cantidad)
    if cantidad>0:    
        while i<cantidad:
            i+=1
            valores=input(f"Digite el valor # {i}:\t")
            
            if es_numerico(valores) == True:
                valores=float(valores)
                if valores<0:
                    contadornegativos=contadornegativos+1
                else:
                    contadorpositivos=contadorpositivos+1
            else:
                print ("El valor digitado no corresponde a un dato númerico")
                break
        print (f"La cantidad de número positivos digitados es de {contadorpositivos} y la cantidad de números negativos es de {contadornegativos}")
    else:
        print ("El valor digitado no puede ser cero o menor")
else:
    print ("El valor digitado no es un valor valido (debe ser un número entero positivo mayor que cero)")
