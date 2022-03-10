import os
os.system ("cls")

print("Realiza el cálculo del salario de 1500$ con el aumento anual de un 10%")
salario1=1500
aumentoanual=0

for i in range(1,7):
    aumentoanual = salario1*1.1
    print (f"Salario año {i} = {aumentoanual}$")
    salario1=aumentoanual