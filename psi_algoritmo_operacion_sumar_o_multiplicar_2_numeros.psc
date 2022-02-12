Algoritmo sumar_multiplicar
	Definir dato1,dato2 Como Real
	Definir operacion,salir Como Caracter
	Escribir 'Digite dos datos numericos, para realizar la operación de sumar o multiplicar'
	Escribir ""
	Escribir 'Primer Número'
	Leer dato1
	Escribir 'Segundo Número'
	Leer dato2
	Escribir 'Que operación desea realizar'
	Repetir
		Escribir "Digite una S, para sumar o una M para multiplicar los datos númericos."
		Leer operacion
	Hasta Que operacion='m' O operacion='s'
	Si operacion='s' Entonces
		Escribir 'La sumatoria de los números es: ',dato1+dato2
	SiNo
		Escribir 'La multiplicación de los números es: ',dato1*dato2
	FinSi
FinAlgoritmo
