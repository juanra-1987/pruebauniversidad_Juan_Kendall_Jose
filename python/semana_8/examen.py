import os
os.system ("cls")

usuario = "JUANASTUA"
pasword = "AstuaJR1133"

print ("Bienvenido a su cajero de confianza.")
for i in range (3):
    digiteUsuario=input("Digite su Usuario:")
    digiteUsuario=digiteUsuario.upper()
  
    if digiteUsuario == usuario:
        print (f"Digite la contraseña del usuario {usuario}")
        digitePasword = input ()
        for intento in range (3):
            if digitePasword == pasword:
                print ("Bienvenido a su cajero de confianza")
                opciones = int (input ("Digite la opción que se adecue a su necesidad:\n1-Depositar dinero a la cuenta\t2-Sacar dinero de la cuenta\t3-Ver saldo\t4-Salir\n---> "))

            elif digitePasword != pasword:
                print (f"La contraseña digitada no corresponde al usuario: {usuario}")
                intentopasword= input (f"Desea volver a intentarlo (S/N)\nIntento {intento+1} de 3\n--->")
                intentopasword=intentopasword.upper()
                if intentopasword == "NO" or intentopasword == "N":
                                print ("Vuelva pronto. Hasta luego")
                                i=4
                                break
                else:
                                print (" ")
    else:
        print ("Usuario no se encuentra registrado en la base de datos.") 

print ("Sistema Bloqueado")
    