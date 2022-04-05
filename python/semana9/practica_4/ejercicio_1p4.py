import os
os.system("cls")

import random


i=1
while i<11:
    numeroAzar = random.randint(0,10)
    print (f"{i}- {numeroAzar} el cuadrado es {numeroAzar*numeroAzar} y el cubo es {numeroAzar*numeroAzar*numeroAzar}")
    i=i+1