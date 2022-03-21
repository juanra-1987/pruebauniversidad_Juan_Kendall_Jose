from ast import Break
import os
os.system ("cls")

def multiplo (a,b):
    return True if a % b == 0 else False

usuario = "JUANASTUA"
pasword = "JuanAstua1133"
a=0
intento =0
saldojuan=0
menu1 = True
menu2= True
menu3=True
print ("Bienvenido a su cajero de confianza.")

for i in range (1,5):

    digiteUsuario=input("Digite su Usuario:")
    digiteUsuario=digiteUsuario.upper()

    if digiteUsuario==usuario:

        for intento in range (1,4):
            print (f"Digite la contraseña del usuario {usuario}")
            digitePasword = input ()

            if digitePasword == pasword:
                    print ("Bienvenido a su cajero de confianza")
                    opcion=True                
                    while opcion:
                        while opcion:
                            try:
                                menu = int (input ("Digite la opción que se adecue a su necesidad:\n1-Depositar dinero a la cuenta\t2-Sacar dinero de la cuenta\t3-Ver saldo\t4-Salir\n---> "))                                    
                                opcion==False
                                break
                            except:
                                print ("Está ingresando un valor no valido.")
                                opcion==True

                        
                        if menu==1:
                            print ("\nSu elección es realizar un depósito.")
                            menu1== True
                            while menu1:
                                try:
                                    deposito = int (input (f"Su saldo actual es {saldojuan} colones\nDigite el monto a depositar en colones---> "))
                                    menu1==False 
                                    if multiplo (deposito,1000)==True:
                                        menu1==False
                                        break
                                    else:
                                        menu1==True 
                                        print ("El monto depósitado debe ser multiplo de 1000 colones")                                 
                                except:
                                    print ("Está ingresando un valor no valido.")
                                    menu1==True
                            nuevosaldo=saldojuan+deposito
                            saldojuan=nuevosaldo
                            print (f"\nSu deposito fue de {deposito}\ny su saldo es de {nuevosaldo} colones\n")
                            opcion==True
                            
                        elif menu==2:
                            print ("\nSu elección es retirar dinero.")
                            menu2== True
                            while menu2:
                                try:
                                    retiro = int (input (f"Su saldo actual es {saldojuan} colones\nDigite el monto a retirar en colones---> "))
                                    menu2==False
                                    if multiplo (retiro,1000)==True:
                                        menu1==False
                                        break
                                    else:
                                        menu1==True 
                                        print ("El monto de retiro debe ser multiplo de 1000 colones") 
                                except:
                                    print ("Está ingresando un valor no valido.")
                                    menu2==True
                            nuevosaldo=saldojuan-retiro
                            if nuevosaldo>=0:
                                print (f"\nSu retiro fue de {retiro} colones\ny su saldo es de {nuevosaldo} colones\n")
                                saldojuan=nuevosaldo
                            else:
                                print (f"El monto de retiro supera el saldo actual\n")
                            opcion== True

                        elif menu==3:
                            print ("\nSu elección es ver el sado de su cuenta.")
                            print (f"Su saldo es de {saldojuan} colones")
                            opcion== True
                        elif menu==4:
                            print ("Salir\nHasta la próxima")
                            i=7
                            break
                        else:
                            print ("Por favor digite un valor valido")
                            opcion== True

                        
                    break

            elif digitePasword != pasword and intento < 3:

                    print (f"La contraseña digitada no corresponde al usuario: {usuario}")
                    intentopasword= input (f"Desea volver a intentarlo (S/N)\nIntento {intento} de 3\n--->")
                    intentopasword=intentopasword.upper()

                    if intentopasword == "N":
                        print ("Hasta luego")
                        intento=5
                        a=1
                        break
                        
                    elif intentopasword == "S":
                        continue
                    else:
                        print ("La opción digitada no es valida. Hasta Luego")
                        intento=5
                        a=1
                        break    
            elif digitePasword != pasword and intento == 3:
                print ("Usuario Bloqueado")
                a=1
                break   
        break                     
    elif digiteUsuario!=usuario:

        print ("El usuario digitado no se encuentra en la base de datos del Banco")
    
if i==4 and a== 0:
    print ("Vuelva a intentar en 5 minutos")
    exit
elif intento == 5 and a ==1:
    print ("Mejor suerte para la próxima")  
else:
    print (" ") 