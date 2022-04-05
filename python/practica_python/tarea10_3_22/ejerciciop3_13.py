import os
os.system ("cls")
monto=5
mtotal=0
for i in range (1,21):
    monto1=monto*2
    print (f"El monto a pagar el mes {i} es igual a {monto1} ")
    monto=monto1
    mtotal=monto+mtotal

print (f"El monto total pagado por los 20 meses fue de {mtotal} $")