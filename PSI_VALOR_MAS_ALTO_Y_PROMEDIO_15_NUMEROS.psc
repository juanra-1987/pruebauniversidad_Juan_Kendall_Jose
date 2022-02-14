Algoritmo quince_numros_mayor_promedio
	Definir n,n2,nmayor,nmenor,nm2 Como Real //nm2 número mayor 2
	Escribir 'Se calculara el valor mas alto, el mas bajo y el promedio, de 15 números solicitados'
	Escribir '*************************************************************************************'
	Para i<-1 Hasta 15 Hacer
		Escribir 'Digite el dato número ',i
		Leer n
		Si nmenor<n Entonces
			Si i<2 Entonces
				nm2 <- n
			FinSi
		SiNo
			nm2 = n
		FinSi
		nmenor = nm2
		Si n>nmayor Entonces
			nmayor <- n
		FinSi
		n2 <- n+n2
	FinPara
	Escribir 'El valor mas alto en la serie de números es: ',nmayor
	Escribir 'El valor mas bajo en la serie de números es: ',nm2 //número mayor 2
	Escribir 'El valor promedio es: ',n2/15
FinAlgoritmo
