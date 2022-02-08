Algoritmo Calculo_de_nota_en_letras
	Definir nota Como Real
	Escribir 'Digite la nota obtenida de 1 a 20'
	Leer nota
	Mientras nota>20 o nota<1 Hacer
		Escribir "Digite nuevamente un valor valido entre 1 a 20, ya que el valor  ", nota, "  no es  valido"
		Leer nota
	FinMientras
	Segun nota  Hacer
		1,2,3,4,5,6,7,8:
			Escribir 'Su nota es una E'
		9,10,11,12:
			Escribir 'Su nota es una D'
		13,14,15:
			Escribir 'Su nota es una C'
		16,17,18:
			Escribir 'Su nota es una B'
		19,20:
			Escribir 'Su nota es una A'
		De Otro Modo:
			Escribir 'El valor digitado no esta en el rango solicitado'
	FinSegun
FinAlgoritmo
