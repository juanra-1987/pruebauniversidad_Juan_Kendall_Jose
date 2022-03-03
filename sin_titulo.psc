Algoritmo sin_titulo
	definir contador, cantidad Como Entero
	definir notas,promedio,totalnotas Como Real
	definir condicional Como Caracter
	
	contador=0
	cantidad=0
	promedio=0
	totalnotas=0
	condicional="si"
	
	Mientras condicional=="si" Hacer
		ESCRIBIR "Por favor digite la nota de un estudiante"
		leer notas
		
		totalnotas=totalnotas+notas
		
		ESCRIBIR "Desea continuar  (si/no)"
		Leer condicional
		
		contador=contador+1
		
	Fin Mientras
	Escribir "El total de estudiantes es de: ", contador
	Escribir "El promedio de las notas es de: ",totalnotas/contador
	
	//para contador=1 hasta 10 con paso 1 Hacer
	//	contador
	//FinPara
	
FinAlgoritmo
