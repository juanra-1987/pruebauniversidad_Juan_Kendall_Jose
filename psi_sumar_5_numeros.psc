Algoritmo sumar_5_numeros
	Definir n1,n2,n3,n4,n5 Como Real
	Definir denuevo Como Caracter
	Repetir
		Escribir 'Digite 5 números, los cuales se sumaran'
		Escribir '***********************************************'
		Escribir 'Número 1'
		Leer n1
		Escribir 'Número 2'
		Leer n2
		Escribir 'Número 3'
		Leer n3
		Escribir 'Número 4'
		Leer n4
		Escribir 'Número 5'
		Leer n5
		Escribir 'La suma de ',n1,'+',n2,'+',n3,'+',n4,'+',n5,'=',n1+n2+n3+n4+n5
		Repetir
			Escribir 'Gracias, quieres repetir el proceso (s/n)'
			Leer denuevo
		Hasta Que denuevo="s" o denuevo="n"
	Hasta Que denuevo='n'
FinAlgoritmo
