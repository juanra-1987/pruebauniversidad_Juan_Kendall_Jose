import os
os.system ("cls")

print ("Cálculo de ganancias según inversión")
invertir=float(input("Digite la cantidad a invertir en colones: "))
interes=float(input("Digite la tasa de interes anual: "))
tiempo=int(input("Digite la cantidad de años de la inversión: "))
print ("\n")
for i in range (1,tiempo+1,1):
        valorFuturo = invertir * (pow(1+((interes)/100),i))
        print(f"En el Año {i} el monto de capitalizado es {valorFuturo}")

print (f"\nSe invirtio {invertir} colones y se obtuvo un total de {valorFuturo-invertir} colones de ganancias en {tiempo} años ")


