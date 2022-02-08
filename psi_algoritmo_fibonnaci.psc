Algoritmo Fibonacci
	Definir final,i,i1,i2 Como Entero
	Escribir 'Se realizará la serie de Fibonacci, hasta el valor de sucesiones que usted elija'
	Escribir 'Escriba el número de sucesiones:'
	Leer final
	i1 <- 0
	i2 <- 1
	para i=1 hasta final Hacer
		Escribir i1
		i3=i1+i2
		i1=i2
		i2=i3
	Finpara
FinAlgoritmo
