import os
os.system ("cls")

print ("Determina el costo de la cita, según la cantidad de citas realizadas")
numCita=int(input("Digite el número de cita a la cual va a asistir: "))

if numCita>0 and numCita<=3:
    print ("El monto de la consulta es de 200$")
    total=numCita*200
elif numCita>=4 and numCita<=5:
    print ("El monto de la consulta es de 150$")
    total=600+(numCita-3)*150
elif numCita>=6 and numCita<=8:
    print ("El monto de la consulta es de 100$")
    total=900+(numCita-5)*100
elif numCita>=9 and numCita<=100:
    print ("El monto de la consulta es de 100$")
    total=900+(numCita-5)*100
else:
    print ("El valor digitado está incorrecto")

print (f"El monto invertido incluyendo la cita #{numCita} es de {total}$")