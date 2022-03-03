Algoritmo algoritmo_d_examen_1
	definir horastrabajadas,horastotal como entero
	Definir precio Como Real
	ESCRIBIR "Cáluculo de Sueldo por horas trabajadas"
	Escribir ""
	Escribir "Digite la cantidad de horas trabajadas"
	Para i=1 Hasta 6 Con Paso 1 Hacer
		Escribir "Horas del día ", i
		Leer horastrabajadas
		horastotal=horastrabajadas+horastotal
	Fin Para
	Escribir "Digite el precio a pagar por hora"
	Leer precio
	Escribir "El total de horas trabajadas fue de ", horastotal, " y el sueldo total es: ",horastotal*precio
FinAlgoritmo
