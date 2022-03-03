import os
os.system ("cls")

print ("Cálculo de salario por horas trabajadas")
horasTrabajadas = float(input("Digite la cantidad de horas trabajadas en la semana:\n "))
precioHora = float(input("Salario por hora:\n "))

if horasTrabajadas> 48:
    print (f"El salario devengado:\n {precioHora*48} colones por jornada de 48 horas\n {1.5*precioHora*(horasTrabajadas-48)} colones por {horasTrabajadas-48} horas extra")
    print (f"Total {48*precioHora+(horasTrabajadas-48)*precioHora*1.5} colones")
else:
    print (f"El salario devengado es de:\n {precioHora*horasTrabajadas} colones por {horasTrabajadas} horas trabajadas")