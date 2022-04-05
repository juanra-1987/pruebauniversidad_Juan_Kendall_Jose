import os
os.system("cls")

#def pesobovino():
    
trymenuSeleccion=True
print ("***********************  Bienvenido productor Pecuario  ***********************\nEn nuestra base de datos hasta el momento podemos trabjar para Ganado Bovino, Ovino y Porcino")
while trymenuSeleccion:
    try:
        menuSeleccion=int(input("\nPor favor elija una de las siguientes opciones:\n1.Conocer el precio de compra o venta animales de producción.\n2.Conocer el peso estimado de sus animales a partir de sus dimensiones y edades.\n3.Creadores del Proyecto\n4.Salir\n-->"))
        trymenuSeleccion=False
        a=1
    except:
        print ("\nEl dato ingresado no corresponde a: 1,2,3 ó 4\nIntente de nuevo.")   
        trymenuSeleccion=True
        a=0

    if a==1:
        if menuSeleccion==1:
            print ("Entro al menu 1")
            print ("Por favor digite la epoca del año que desea comprar y vender:\n1.Verano \n2.Invierno")
        elif menuSeleccion==2:
            print ("Entro al menu 2")
        elif menuSeleccion==3:
            print ("\nEntro al menu 3\nLos creadores de este programa son los Ing.Juan Rafael, Ing.Kendall y el Ing.José\nPara nosotros es un placer servirles, vuelva a elegir la opción que más se le adecue.")
            trymenuSeleccion=True
        elif menuSeleccion==4:
            print ("Entro al menu 4\nHasta la próxima")
            break
        else:
            print ("Los valores deigitados deben ser 1,2,3 o 4")
            trymenuSeleccion=True


