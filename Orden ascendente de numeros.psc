Algoritmo orden_ascendente_de_numeros
	Definir numero1, numero2, numero3 como real 
	Repetir
		Escribir "Coloque tres numeros todos Diferentes para ordenarlos de menor a mayor"
		Escribir "Digite el numero 1"
		Leer numero1
		Escribir "Digite el numero 2 "
		Leer numero2
		Escribir "Digite el numero 3 "
		Leer numero3 
	Hasta Que numero1<>numero2 y numero1<>numero3 y numero2<>numero3 
	Si numero1>numero2 y numero1>numero3  Entonces
		Si numero2>numermo3 Entonces
			Escribir "El orden es: "
			Escribir numero3
			Escribir numero2
			Escribir numero1 
		SiNo
			Escribir "El orden ascendente es: "
			Escribir numero2 
			Escribir numero3
			Escribir numero1
		FinSi
	SiNo
		Si numero2>numero1 y numero2>numero3 Entonces
			Si numero1>numero3 Entonces
				Escribir "El orden ascendente es: "
				Escribir numero1
				Escribir numero2
				Escribir numero3
			SiNo
				Escribir "El orden ascendente es: "
				Escribir numero3
				Escribir numero1
				Escribir numero2
			FinSi
		SiNo
			Si numero2>numero1 Entonces
				Escribir "El orden ascendente es: "
				Escribir numero1
				Escribir numero2
				Escribir numero3 
			SiNo
				Escribir "El orden ascendente es: "
				Escribir numero2
				Escribir numero1
				Escribir numero3
			FinSi
		FinSi
	FinSi
FinAlgoritmo
