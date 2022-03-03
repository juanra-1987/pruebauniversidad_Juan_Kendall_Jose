print("Digite dos números")
numero1=int(input("Digite número "))
numero2=int(input("Digite número "))
numero3=int(input("Digite número "))

if (numero1>numero2)and(numero1>numero3):
    print("El número 1 es el mayor de todos")
else:
    if (numero2>numero1)and (numero2>numero3):
        print("El número 2 es el mayor")
    else:
        print("El mayor es el 3")



#if numero1>numero2:
#    print("El número 1 es mayor que el número 2")
#else:
#    print("El número 2 es mayor")        
#if numero2>numero1:
#    print("El número 2 es mayor que el número 1")