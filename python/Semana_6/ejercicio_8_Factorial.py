import os
os.system ("cls")

print ("Digite un número para obtener el factorial de este:")

factorial = int(input())

resultado=1

for i in range (2,factorial+1):
    resultado = resultado * i
     
print (resultado)


