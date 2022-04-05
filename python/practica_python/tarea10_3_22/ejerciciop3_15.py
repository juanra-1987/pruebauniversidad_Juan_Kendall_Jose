import os
os.system ("cls")

print ("Imprime una escalera de numbers")
altura=int(input("Digite la altura en number hasta donde donde se quiere que llegue la escalera:\t"))

for fila in range(1,altura+1):
    for columna in range (1,fila+1):
        print (columna,end="")
    print ("")
