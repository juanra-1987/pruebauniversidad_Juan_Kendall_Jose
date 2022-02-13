Algoritmo orden_ascendente_3_numeros
	Definir n1,n2,n3 Como Real
	Repetir
		Escribir 'Digite tres números DISTINTOS que se ordenarán de menor a mayor'
		Escribir ''
		Escribir 'Digite el primer número'
		Leer n1
		Escribir 'Digite el segundo número'
		Leer n2
		Escribir 'Digite el tercer número'
		Leer n3
	Hasta Que n2<>n3 y n2<>n1 y n1<>n3
	Si n1>n2 Y n1>n3 Entonces
		Si n2>n3 Entonces
			Escribir 'El orden ascendente es:'
			Escribir n3
			Escribir n2
			Escribir n1
		SiNo
			Escribir 'El orden ascendente es:'
			Escribir n2
			Escribir n3
			Escribir n1
		FinSi
	SiNo
		Si n2>n1 Y n2>n3 Entonces
			Si n1>n3 Entonces
				Escribir 'El orden ascendente es:'
				Escribir n3
				Escribir n1
				Escribir n2
			SiNo
				Escribir 'El orden ascendente es:'
				Escribir n1
				Escribir n3
				Escribir n2
			FinSi
		SiNo
			Si n2>n1 Entonces
				Escribir 'El orden ascendente es:'
				Escribir n1
				Escribir n2
				Escribir n3
			SiNo
				Escribir 'El orden ascendente es:'
				Escribir n2
				Escribir n1
				Escribir n3
			FinSi
		FinSi
	FinSi
FinAlgoritmo
