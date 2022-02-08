Algoritmo sin_titulo
	definir horastrabajadas,precio,salario,extra,salariototal como real
	definir seleccion como caracter
	Escribir "Cuantos trabajadores desea calcular el salario"
	seleccion = "si"
	salariototal = 0
	Trabajadores = 0
	Mientras seleccion="si" o seleccion="s" Hacer
		Escribir "Digita las horas trabajadas y el precio por hora"
		Escribir "horas trabajadas"
		Leer horastrabajadas
		Escribir "Precio por hora"
		Leer precio
		Si horastrabajadas>40 Entonces
			extra = horastrabajadas-40
			salario=(40*precio+(1.5*(extra*precio)))
		SiNo
			salario = horastrabajadas*precio
		FinSi
		Escribir "El salario es: ", salario
		salariototal = salario+salariototal
		trabajadores = trabajadores+1
		Escribir "Desea continuar? (si/no)"
		Leer seleccion
		Mientras seleccion<>"si" o seleccion<>"no" Hacer
			Escribir "Por favor digitar correctamente si o no"
		FinMientras
	FinMientras
FinAlgoritmo
