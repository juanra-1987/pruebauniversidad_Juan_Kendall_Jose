import os
os.system ("cls")

print ("Calcula el bono a recibir según antiguedad o salario")
sueldo = float(input("Digite el salario percibido en la empresa:\t "))
antiguedad = float(input("Digite los años de servicio en la empresa:\t "))

if antiguedad>=2 and antiguedad<=5:
    aumentAntiguedad=sueldo*.2
elif antiguedad>5:
    aumentAntiguedad=sueldo*.3
if sueldo<1000:
    aumentsueldo=sueldo*.25
elif sueldo>=1000 and sueldo<=3500:
    aumentsueldo=sueldo*.15
elif sueldo>3500:
    aumentsueldo=sueldo*.1

if aumentsueldo>aumentAntiguedad:
    print(f"El monto del bono por sueldo es de {aumentsueldo}")
else:
    print(f"El monto del bono por antiguedad es de {aumentAntiguedad}")