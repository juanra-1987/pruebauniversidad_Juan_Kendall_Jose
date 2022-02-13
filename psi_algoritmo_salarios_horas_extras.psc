Algoritmo sin_titulo
	Definir horastrabajadas,precio,salario,extra,salariototal Como Real
	Definir seleccion Como Caracter
	Escribir 'Cálculo de salario según horas trabajadas por semana'
	Escribir ' ***********************************************************'
	seleccion <- 'si'
	salariototal <- 0
	trabajadores <- 0
	Mientras seleccion='si' Hacer
		extra = 0
		Escribir 'Digita las horas trabajadas por semana y el precio por hora'
		Escribir '***************************'
		Escribir 'horas trabajadas'
		Leer horastrabajadas
		Escribir 'Precio por hora'
		Leer precio
		Si horastrabajadas>40 Entonces
			extra <- horastrabajadas-40
			salario <- (extra*1.5+40)*precio
		SiNo
			salario <- horastrabajadas*precio
		FinSi
		Escribir 'El salario devengado es: ',salario,' con ',extra,' horas extras trabajadas'
		salariototal <- salario+salariototal
		trabajadores <- trabajadores+1
		Repetir
			Escribir 'Desea continuar otro cálculo? (si/no)'
			Leer seleccion
		Hasta Que seleccion='si' O seleccion='no'
	FinMientras
FinAlgoritmo
