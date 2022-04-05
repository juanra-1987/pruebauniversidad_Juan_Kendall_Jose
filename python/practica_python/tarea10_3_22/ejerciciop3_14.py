import os
os.system ("cls")

contarverde=0
contarblanco=0
contarrojo=0

print ("Contabiliza los focos (N cantidad) según color (A-Verde (V) B-Blanco (B) C-Rojo (R")
nFocos=int(input("Digite la cantidad de focos a clasificar: "))

for i in range(1,nFocos+1):
    color=str(input(f"Digite el color del foco # {i}: \t"))
   
    color=color.upper()

    if color=="A" or color=="VERDE" or color=="V":
        contarverde=1+contarverde
    elif color=="B" or color=="BLANCO" or color=="B":
        contarblanco=1+contarblanco
    elif color=="C" or color=="ROJO" or color=="R":
        contarrojo=1+contarrojo

print (f"El total de focos es {nFocos} y se clasifican de la siguiente forma:\n1-Focos Verdes:    \t{contarverde}\n2-Focos Blancos:\t{contarblanco}\n3-Focos Rojos:   \t{contarrojo}")