import os
os.system ("cls")

usuarios = {
            "JUANASTUA":"Astua111",
            "RONALDARIAS":"Arias222",
            "MARICELAGUADAMUZ":"Guadamuz333",
            "LUISVARGAS":"Vargas444"
}

for i in range (3):
    digiteUsuario=input("Digite su Usuario:")
    digiteUsuario=digiteUsuario.upper()
  
    if digiteUsuario == usuarios:
        print (f"Digite la contraseña del usuario {usuarios}")
        digitePasword = input ()
        for intento in range (3):
            if digitePasword == pasword:
                print ("Bienvenido a su cajero de confianza")
                opciones = int (input ("Digite la opción que se adecue a su necesidad:\n1-Depositar dinero a la cuenta\t2-Sacar dinero de la cuenta\t3-Ver saldo\t4-Salir\n---> "))

            else:
                print (f"La contraseña digitada no corresponde al usuario: {usuarios}")
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
if i == 4:
     print ("Hasta Pronto")
     
else:
    print ("Sistema Bloqueado")