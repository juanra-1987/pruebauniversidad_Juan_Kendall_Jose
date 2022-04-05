class Fraccion:
    num = 2
    den =3 
    

    def __init__ (self,n,d):
        self.num=n
        self.den=d
        

    def imprime(self):
        print (self.num,"/", self.den)

    def multiplicar(self,b):
        n = self.num * b.num
        d = self.den * b.den
        r = Fraccion (n,d)
        return r



def main ():

    a = Fraccion(3,2)
    a.imprime()

    b = Fraccion(7,4)
    b.imprime()

    r = b.multiplicar (a)
    r.imprime()
if __name__== "__main__":
    main()