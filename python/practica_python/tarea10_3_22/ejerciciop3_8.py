import os
os.system ("cls")

print ("Bienvenidos EL OSO HAMBRIENTO")

hamburguesa=int(input("Digite la cantidad de Hamburguesas a comprar: "))
combo=int(input("Digite en número del tipo de Hamburguesa a ordenar\n1-Sencillas\t20$\n2-Doble    \t25$\n3-Triple\t28$\n-->"))
pago=int(input("Digite en número del modo de pago:\n1-Efectivo\n2-Tarjeta de Crédito\n-->"))


if combo==1:
    if pago==1:
        total=hamburguesa*20
        print (f"El total a pagar es de {total}$")
    elif pago==2:
        total=hamburguesa*20*1.05
        print (f"El total a pagar es de {total}$")
elif combo==2:
    if pago==1:
        total=hamburguesa*25
        print (f"El total a pagar es de {total}$")
    elif pago==2:
        total=hamburguesa*25*1.05
        print (f"El total a pagar es de {total}$")
if combo==3:
    if pago==1:
        total=hamburguesa*28
        print (f"El total a pagar es de {total}$")
    elif pago==2:
        total=hamburguesa*28*1.05
        print (f"El total a pagar es de {total}$")
