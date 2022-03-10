import os
os.system ("cls")

def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

print ("Digite la cantidad de empleados de la empresa")
cantidad=int(input("Número de empleados: "))
i=0
salariomayor=0
salariomenor=0
while i<cantidad:
            i+=1
            salario=input(f"Digite el salario del empleado # {i}:\t")
            
            if es_numerico(salario) == True:
                salario=float(salario)

                if salario<1500 and salario>=1000:
                    salariomenor=salariomenor+1
                elif salario<1000 or salario>2000:
                    print ("Los salario de la empresa oscilan entre 1000 a 2000 Dolares, revise el valor digitado.")
                    break
                else:
                    salariomayor=salariomayor+1
            else:
                print ("El valor digitado no corresponde a un dato númerico")
                break
print (f"La cantidad de salarios\nmayores a 1500 dolares son {salariomayor} \nmenores a 1500 dolares son {salariomenor}")