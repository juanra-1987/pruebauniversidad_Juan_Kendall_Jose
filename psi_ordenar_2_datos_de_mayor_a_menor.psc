Algoritmo ordenar_2_datos_de_mayor_a_menor
	Definir dato1,dato2 Como Real
	Repetir
		Escribir 'Escriba dos datos númericos DIFERENTES que se ordenaran de mayor a menor'
		Escribir 'Digite el primer número'
		Leer dato1
		Escribir 'Digite el segundo número'
		Leer dato2
	Hasta Que dato1<>dato2
	Si dato1>dato2 Entonces
		Escribir 'El orden de mayor a menor es'
		Escribir dato1
		Escribir dato2
	SiNo
		Escribir 'El orden de mayor a menor es'
		Escribir dato2
		Escribir dato1
	FinSi
FinAlgoritmo
