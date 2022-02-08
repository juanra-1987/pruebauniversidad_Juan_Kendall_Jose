Algoritmo sin_titulo
	definir Nota como entero
	Escribir "Escriba la nota del 1 al 20"
	Leer nota
	Si nota<=9 Entonces
		Escribir "Su nota es una E"
	SiNo
		Si nota>9 y nota<=12 Entonces
			Escribir "Su nota es una D"
		SiNo
			Si nota>12 y nota <=15 Entonces
				Escribir "Su nota es una C"
			SiNo
				Si nota>15 Y nota<=18 Entonces
					Escribir "Su nota es una B"
				SiNo
					Si nota>18 y nota<=20 Entonces
						Escribir "Su nota es una A"
					SiNo
						Escribir "El Valor digitado no esta dentro del rango valido"
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	// 
FinAlgoritmo
