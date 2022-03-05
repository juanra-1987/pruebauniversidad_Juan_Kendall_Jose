import os
os.system ("cls")

def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
print ("Determina si debe tributar una persona, según su edad e ingresos.")
edad=input("Digite su edad (números):\n") 
ingreso=input("Digite sus ingresos mensuales en Euros (números):\n")
edad=int(edad)
ingreso=float(ingreso)

if es_numerico(edad) == True and es_numerico(ingreso) == True and ingreso>0:
    if edad>16 and ingreso >= 1000:
        print ("Según su condicion de edad y salario, debe TRIBUTAR")
    else:
        print ("Según su condicion de edad y salario, NO debe tributar")
else:
    print ("Alguno o ambos datos ingresados, no corresponden según lo solicitado")
