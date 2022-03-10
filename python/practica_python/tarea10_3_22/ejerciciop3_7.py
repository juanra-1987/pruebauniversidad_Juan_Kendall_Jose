import os
os.system ("cls")

print ("Determina la cantidad a cobrar a cada alumno según los estudiantes a viajar")
cantidad=int(input("Digite la cantidad de estudiantes a asistir: "))
if cantidad >=100 and cantidad < 1000:
    print ("El costo unitario a cobrar a cada alumno es de 65$")
elif cantidad >= 50 and cantidad < 99:
    print ("El costo unitario a cobrar a cada alumno es de 70$")
elif cantidad >= 30 and cantidad < 49:
    print ("El costo unitario a cobrar a cada alumno es de 95$")
elif cantidad > 0 and cantidad < 29:
    print (f"El costo total del autobus es de 4000$, a cada alumno se le cobrará {4000/cantidad} $")
else:
    print ("El valor digitado está incorrecto. ")