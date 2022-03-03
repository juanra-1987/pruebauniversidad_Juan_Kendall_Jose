import os
os.system ("cls")

import turtle

turtle.setup(800,800)

ventana = turtle.Screen()
lados = int( input("digite la cantidad de lados del polígo regular: "))
for item in range (0,lados):
    turtle.forward(10)
    turtle.left(360/lados)

ventana.exitonclick()

#turtle.donecls
