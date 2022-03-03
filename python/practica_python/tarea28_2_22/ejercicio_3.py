import os
os.system ("cls")

print ("Salario a pagar a empleados por días trabajados")
salarioDia = float(input("Digite el salario por día:\n "))
diasTrabajados = float(input("Digite la cantidad de días trabajados: \n "))

salario = salarioDia * diasTrabajados

print ("El salario bruto del empleado es: ", salario, " colones")

print (f"Rebajos\n10% por pensión {salario*.1} colones\n15% por salud {salario*.15} colones ")
print ("Salario Liquido del Empleado es: ", salario*.75, " colones")