Algoritmo algoritmo_a
	Definir usuario,contraseña Como caracter //
	Definir n Como Entero
	Escribir "Ingreso al sistema Super"
	Escribir ""
	Para i<-1 Hasta 3 Hacer
		Escribir 'Digite su usario: '
		Leer usuario
		Escribir 'Digite su contraseña: '
		Leer contraseña
		Si (usuario="pepe" Y contraseña="supercontraseña") Entonces
			Escribir 'Usuario y contraseña correctos. Puede ingresar al sistema Super'
			i <- 3
			n <- 1
		SiNo
			BORRAR PANTALLA
			Escribir 'Acceso denegado!!!'
		FinSi
	FinPara
	Si n=1 Entonces
		Escribir '************Bienvenido************'
	SiNo
		Escribir 'Sistema Bloqueado, consulte con el Administrador'
	FinSi
FinAlgoritmo
