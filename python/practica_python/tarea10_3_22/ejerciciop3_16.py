import os
os.system ("cls")

print ("Realiza una piramide de asteriscos con la altura que se le indique")
altura=int(input("Digite la altura de la piramide:\t"))

for i in range(altura):
    print(" " * (altura-i-1)+"*"*(2*i+1))

