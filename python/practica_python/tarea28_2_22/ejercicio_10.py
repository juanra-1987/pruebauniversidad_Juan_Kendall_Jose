from ast import AsyncFunctionDef
import os
os.system ("cls")

print("Elija su candidao de preferencia\nA) Candidato Rojo\nB) Candidato Verde \nC) Candidato Azul")
i=0

while i<3:

    eleccion=input("Digite su elección: ").upper()

    if eleccion=="A" or eleccion=="ROJO" or eleccion=="CANDIDATO ROJO":
            print("Usted ha votado por el partido color Rojo")
            break
    elif eleccion=="B" or eleccion=="VERDE" or eleccion=="CANDIDATO VERDE":
            print("Usted ha votado por el partido color Verde")
            break
    elif eleccion=="C" or eleccion=="AZUL" or eleccion=="CANDIDATO AZUL":
            print("Usted ha votado por el partido color Azul")
            break
    else:
            print("Opción Errónea")
            i=i+1


