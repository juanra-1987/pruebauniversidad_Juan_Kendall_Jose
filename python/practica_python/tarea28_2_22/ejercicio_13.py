import os
os.system ("cls")

def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
print ("Digite las dimesiones de los tres lados de un triángulo:")
print ("Se determinará que tipo de triángulo es, según las dimensiones de sus lados:")
a=input("Digite el lado A:\t")
b=input("Digite el lado B:\t")
c=input("Digite el lado C:\t")

if es_numerico(a) == True and es_numerico(b) == True and es_numerico(c) == True :
    a=float(a)
    b=float(b)
    c=float(c)
    if  a>0 and b >0 and c >0:  
        if a==b and a==c:
            print ("No es un triángulo rectángulo\nEl triángulo espécificado es EQUILATERO") 
        elif a==b or b==c or c==a:
            if (b*b+c*c)==a*a:
                print ("El triángulo espécificado es un triángulo rectángulo") 
            else:
                print ("No es un triángulo rectángulo")
            print ("El triángulo espécificado es un ISÓCELES")
        elif a>b and a>c and a<b+c:
            if (b*b+c*c)==a*a:
                print ("El triángulo espécificado es un triángulo rectángulo") 
            else:
                print ("No es un triángulo rectángulo") 
            print ("El triángulo espécificado es un triango ESCALENO")
        elif b>=a and b>=c and b<a+c:
            if (a*a+c*c)==b*b:
                print ("El triángulo espécificado es un triángulo rectángulo") 
            else:
                print ("No es un triángulo rectángulo") 
            print ("El triángulo espécificado es un triango ESCALENO")
        elif c>=a and c>=b and c<a+b:
            if (a*a+b*b)==c*c:
                print ("El triángulo espécificado es un triángulo rectángulo") 
            else:
                print ("No es un triángulo rectángulo") 
            print ("El triángulo espécificado es un triango ESCALENO")
        else:
            print ("Con las dimensiones específicadas no se puede formar un triángulo, los dos lados mas pequeños deben sumar más que el lado mas grande")     
    else:
            print("Los datos ingresado deben ser números reales MAYORES A CERO")        
else:
    print ("Los datos ingresado deben ser NÚMEROS reales positivos")