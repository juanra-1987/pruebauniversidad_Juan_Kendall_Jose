Algoritmo sin_titulo
	Definir horastrabajadas,precio,salario,extra,salariototal Como Real
	Definir seleccion Como Caracter
	Escribir 'Cálculo de salario según horas trabajadas por semana'
	Escribir lista_de_expresiones
	seleccion <- 'si'
	salariototal <- 0
	trabajadores <- 0
	Mientras seleccion='si' O seleccion='s' Hacer
		Escribir 'Digita las horas trabajadas por semana y el precio por hora'
		Escribir lista_de_expresiones
		Escribir 'horas trabajadas'
		Leer horastrabajadas
		Escribir 'Precio por hora'
		Leer precio
		Si horastrabajadas>40 Entonces
			extra <- horastrabajadas-40
			salario <- (40*precio+(1.5*(extra*precio)))
		SiNo
			salario <- horastrabajadas*precio
		FinSi
		Escribir 'El salario devengado es: ',salario,' con ',extra,' horas extras trabajadas'
		salariototal <- salario+salariototal
		trabajadores <- trabajadores+1
		Escribir 'Desea continuar otro calculo? (si/no)'
		Leer seleccion
		Mientras seleccion<>'si' O seleccion<>'no' Hacer
			Escribir 'Por favor digitar correctamente si o no'
			Leer seleccion
		FinMientras
	FinMientras
FinAlgoritmo
