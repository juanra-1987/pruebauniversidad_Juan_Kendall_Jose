import os
os.system ("cls")



print ("cantidad de trabajadores")
cantidad = int(input())
resultado = 0

for i in range (cantidad):
    print ("trabajador",i+1)
    salario = int(input())
    resultado = resultado + salario 
    print ("E")

print ("El total de salario es : ",resultado)
