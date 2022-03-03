Algoritmo ciclo_para
	
	Definir n,numeroempleado,numeroempleadomayor Como Entero
	Definir sueldo,sueldomayor Como Real
	sueldomayor <- 0
	Escribir 'Cantidad de empleados'
	Leer n
	Para i<-1 Hasta n Hacer
		Escribir 'Número del empleado:'
		Leer numeroempleado
		Escribir 'Sueldo del empleado'
		Leer sueldo
		Si sueldo>sueldomayor Entonces
			sueldomayor <- sueldo
			numeroempleadomayor <- numeroempleado
		FinSi
	FinPara
	Escribir 'El empleado con el mayor sueldo es:'
	Escribir 'numero de empleado: ',numeroempleadomayor,' y su sueldo es: ',sueldomayor
FinAlgoritmo
