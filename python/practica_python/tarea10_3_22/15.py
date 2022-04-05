import os
os.system ("cls")

cantidad=int(input("Digite la altura en number hasta donde donde se quiere que llegue la escalera:\t"))

numColumna=0

while numColumna<cantidad:
    fila=numColumna+1
    cont=0
    m=""
    while(cont<fila):
        m=m+str(numColumna+1)+" " # si no necesitas el espacio, seria m=m+str(numcol+1)
        cont+=1
    print (m)
    numColumna=numColumna+1