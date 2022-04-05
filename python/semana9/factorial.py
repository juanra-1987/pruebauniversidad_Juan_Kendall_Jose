def factorial(numero):
    print ("Valor incial, ", numero)
    if numero>1:
        numero = numero * factorial (numero-1)
    print ("valor final, ", numero)
    return numero

print (factorial(5))
