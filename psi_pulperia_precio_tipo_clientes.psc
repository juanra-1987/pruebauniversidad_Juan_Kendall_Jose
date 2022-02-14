Algoritmo pulperi_descuento_tipo_cliente
	Definir tiponumero,precio,pagar Como Real
	Definir nombrecliente,tipo Como Caracter
	Escribir 'Cálculo del monto a cancelar según tipo de Cliente (Tipo A, B o C)'
	Escribir '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
	Escribir 'Digite el nombre del Cliente'
	Leer nombrecliente
	Escribir 'Digite el tipo de cliente que es (A,B o C)'
	Leer tipo
	Escribir 'Digite el monto de la compra:)'
	Leer precio
	Si tipo="a" Entonces
		tiponumero <- 1
	SiNo
		Si tipo='b' Entonces
			tiponumero <- 2
		SiNo
			Si tipo='c' Entonces
				tiponumero <- 3
			FinSi
		FinSi
	FinSi
	Segun tiponumero  Hacer
		1:
			pagar <- precio*0.60
			Escribir 'Don (Doña) ',nombrecliente,' cancela: ',pagar,' colonesse se le aplico un 40% de descuento'
		2:
			pagar <- precio*0.70
			Escribir 'Don (Doña) ',nombrecliente,' cancela: ',pagar,' colonesse se le aplico un 30% de descuento'
		3:
			pagar <- precio*0.95
			Escribir 'Don (Doña) ',nombrecliente,' cancela: ',pagar,' colonesse le aplico un 5% de descuento'
		De Otro Modo:
			Escribir 'No selecciono dentro de la catergoría por tanto no tiene descuento'
			Escribir 'Don (Doña) ',nombrecliente,' cancela: ',precio,' colones, no se le aplicó descuento'
	FinSegun
FinAlgoritmo
