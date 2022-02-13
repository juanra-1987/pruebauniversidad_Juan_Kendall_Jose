Algoritmo cantidad_de_numeros_enteros_entre_0_y_n
	definir n,numenteros como real
	Mientras n<=0 Hacer
		escribir "Digite un número real mayor a 0 para determinar la cantidad de números enteros comprendidos entre cero y el número elegido"
		leer n
	Fin Mientras
	numenteros= redon(n)
	si n>numenteros Entonces
		Escribir "La cantidad de números enteros entre 0 y ", n " es de ", numenteros
	SiNo
		Escribir "La cantidad de números enteros entre 0 y ", n " es de ", numenteros-1
	FinSi
	
	
FinAlgoritmo
