import os
os.system("cls")




jugadores = {

1 : "Casillas", 15 : "Ramos",

3 : "Pique", 5 : "Puyol",

11 : "Capdevila", 14 : "Xabi Alonso",

16 : "Busquets", 8 : "Xavi Hernandez",

18 : "Pedrito", 6 : "Iniesta",

7 : "Villa"

}



numJugador = int (input (" Digite el número de Jugador: "))

#print (numJugador in jugadores)

if numJugador in jugadores:
    print (f"El número {numJugador}"," es de: ",jugadores[numJugador])
else:
    print ("El número digitado no corresponde a ningún jugador en nuestra lista")
