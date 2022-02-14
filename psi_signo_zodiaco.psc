Algoritmo signo_zodiaco
	// Aries	21 de marzo ? 20 de abril
	// Tauro	21 de abril ? 21 de mayo	
	// Géminis	22 de mayo ? 21 de junio
	// Cáncer	22 de junio ? 22 de julio	
	// Leo	23 de julio ? 22 de agosto	
	// Virgo	23 de agosto ? 22 de septiembre
	// Libra	23 de septiembre ? 22 de octubre
	// Escorpio	23 de octubre ? 22 de noviembre
	// Sagitario	23 de noviembre ? 21 de diciembre
	// Capricornio	22 de diciembre ? 20 de enero
	// Acuario	21 de enero ? 18 de febrero	
	// Piscis	19 de febrero ? 20 de marzo
	// dia de nacimiento = d
	// mes de nacimeinto = m
	Definir m,d,diasmes Como Entero
	Escribir 'Signo del zodiaco a partir de su mes y día de nacimiento'
	Escribir ''
	Escribir 'Digite su mes de nacimiento (en número)'
	Leer m
	Escribir 'Digite su día de nacimiento (en número)'
	Leer d
	Si m<1 O m>12 Entonces
		Escribir 'Error en el mes de nacimiento (Rango del 1 al 12)'
	SiNo
		Si m=1 O m=3 O m=5 O m=7 O m=8 O m=10 O m=12 Entonces
			diasmes <- 31
		SiNo
			Si m=2 Entonces
				diasmes <- 29
			SiNo
				diasmes <- 30
			FinSi
		FinSi
		Si d<=diasmes Entonces
			Si m=3 Y d>=21 O m=4 Y d<=20 Entonces
				Escribir 'Su signo del Zodiaco es Aries'
			FinSi
			Si m=4 Y d>=21 O m=5 Y d<=21 Entonces
				Escribir 'Su signo del Zodiaco es Tauro'
			FinSi
			Si m=5 Y d>=22 O m=6 Y d<=21 Entonces
				Escribir 'Su signo del Zodiaco es Gémenis'
			FinSi
			Si m=6 Y d>=22 O m=7 Y d<=22 Entonces
				Escribir 'Su signo del Zodiaco es Cáncer'
			FinSi
			Si m=7 Y d>=23 O m=8 Y d<=22 Entonces
				Escribir 'Su signo del Zodiaco es Leo'
			FinSi
			Si m=8 Y d>=23 O m=9 Y d<=22 Entonces
				Escribir 'Su signo del Zodiaco es Virgo'
			FinSi
			Si m=9 Y d>=23 O m=10 Y d<=22 Entonces
				Escribir 'Su signo del Zodiaco es Libra'
			FinSi
			Si m=10 Y d>=23 O m=11 Y d<=22 Entonces
				Escribir 'Su signo del Zodiaco es Escorpio'
			FinSi
			Si m=11 Y d>=23 O m=12 Y d<=21 Entonces
				Escribir 'Su signo del Zodiaco es Sagitario'
			FinSi
			Si m=12 Y d>=22 O m=1 Y d<=20 Entonces
				Escribir 'Su signo del Zodiaco es Capricornio'
			FinSi
			Si m=1 Y d>=21 O m=2 Y d<=18 Entonces
				Escribir 'Su signo del Zodiaco es Acuario'
			FinSi
			Si m=2 Y d>=19 O m=3 Y d<=20 Entonces
				Escribir 'Su signo del Zodiaco es Piscis'
			FinSi
		SiNo
			Escribir 'Error en el día de nacimiento, el mes ',m,' tiene máximo ',diasmes,' días'
		FinSi
	FinSi
FinAlgoritmo
