Algoritmo algoritmo_a
	Definir usuario,contraseņa Como caracter //
	Definir n Como Entero
	Escribir "Ingreso al sistema Super"
	Escribir ""
	Para i<-1 Hasta 3 Hacer
		Escribir 'Digite su usario: '
		Leer usuario
		Escribir 'Digite su contraseņa: '
		Leer contraseņa
		Si (usuario="pepe" Y contraseņa="supercontraseņa") Entonces
			Escribir 'Usuario y contraseņa correctos. Puede ingresar al sistema Super'
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
