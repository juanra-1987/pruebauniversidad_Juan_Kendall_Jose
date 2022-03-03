import os
os.system ("cls")

print ("Cálculo de descuento según monto de la compra")
compra = float(input("Digite el monto de la compra:\n "))

if compra >= 10000 and compra <= 20000:
    print (f"El descuento es de un 10%\nEl total a cobrar es de {compra*.9} colones")
elif compra>20000 and compra <= 50000:
    print (f"El descuento es de un 30%\nEl total a cobrar es de {compra*.7} colones")
elif compra>50000:
    print (f"El descuento es de un 50%\nEl total a cobrar es de {compra*.5} colones")
else:
    print (f"No hay descuento para este monto de compra\nEl total a cobrar es de {compra} colones")
