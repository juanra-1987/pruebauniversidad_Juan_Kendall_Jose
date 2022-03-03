import os
os.system ("cls")
print ("Ingrese dos datos numericos para realizar las cuatro operaciones básicas")
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingreses el segundo número: "))
nsuma = n1+n2
nresta = n1-n2
nmultiplo = n1*n2 
ndivision = n1/n2
print (F"El resultado de la suma de {n1} más {n2} es : ", nsuma) 
print (F"El resultado de la resta de {n1} menos {n2} es : ", nresta) 
print (F"El resultado de la multiplicación de {n1} y {n2} es : ", nmultiplo) 
print (F"El resultado de la división de {n1} entre {n2} es : ", ndivision) 