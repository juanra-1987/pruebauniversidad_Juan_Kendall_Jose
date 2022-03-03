

import os
import random

os.system ("cls")

intentos = 0
numeroAdivinar = random.randint(0,10)

while intentos <=2:
    print ("Digite el número a adivinar")
    numeroddigitado= int(input())

    if numeroddigitado == numeroAdivinar:
        print ("Maquina")
        break
    else :
        print ("sigue intentado")

    intentos = intentos +1