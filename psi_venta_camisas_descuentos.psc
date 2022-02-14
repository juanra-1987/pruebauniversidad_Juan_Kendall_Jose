Algoritmo descuento_por_cantidad_compra_camisas
	Definir n Como Entero // n cantidad de camisas
	Definir montototal,descuento Como Real
	Repetir // cantidad de camisas
		Escribir 'Digitar la cantidad de camisas por comprar'
		Leer n
	Hasta Que n>0
	Escribir 'Digitar el costo total de ',n,' camisa(s)'
	Leer montototal
	Si n>=1 y n<=4 Entonces
		// descuento del 12,5 MOD 
		Escribir "Felicidades por la compra de ",n," camisas, se le realizará un descuento del 12,5%"
		descuento <- montototal*.125
		Escribir 'El total de la compra es de ',montototal,' colones'
		Escribir 'El total del descuento es   ',descuento,' colones'
		Escribir 'El total a pagar es de      ',montototal-descuento,' colones'
	FinSi
	Si n>=5 y n<=8 Entonces
		// descuento del 20 MOD 
		Escribir "Felicidades por la compra de ",n," camisas, se le realizará un descuento del 20%"
		descuento <- montototal*.20
		Escribir 'El total de la compra es de ',montototal,' colones'
		Escribir 'El total del descuento es   ',descuento,' colones'
		Escribir 'El total a pagar es de      ',montototal-descuento,' colones'
	FinSi
	Si n>=9 Entonces
		// descuento del 31,5 MOD 
		Escribir "Felicidades por la compra de ",n," camisas, se le realizará un descuento del 31,5%"
		descuento <- montototal*.315
		Escribir 'El total de la compra es de ',montototal,' colones'
		Escribir 'El total del descuento es   ',descuento,' colones'
		Escribir 'El total a pagar es de      ',montototal-descuento,' colones'
	FinSi
	ESCRIBIR "*****************************************************************"
	eSCRIBIR "******************* GRACIAS, REGRESA PRONTO *********************"
	ESCRIBIR "*****************************************************************"
FinAlgoritmo
