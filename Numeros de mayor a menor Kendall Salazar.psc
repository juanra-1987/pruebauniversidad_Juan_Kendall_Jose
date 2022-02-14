Algoritmo ordenar_datos_de_mayor_a_menor
	Definir numero1,numero2 Como Real
	Repetir
		Escribir "Escriba 2 numeros DISTINTOS para ordenarlos de mayor a menor'
		Escribir "Digite el número 1"
		Leer numero1
		Escribir "Digite el número 2"
		Leer numero2
	Hasta Que numero1<>numero2
	Si numero1>numero2 Entonces
		Escribir 'El orden de mayor a menor es'
		Escribir numero1
		Escribir numero2
	SiNo
		Escribir 'El orden de mayor a menor es'
		Escribir numero2
		Escribir numero1
	FinSi
FinAlgoritmo
