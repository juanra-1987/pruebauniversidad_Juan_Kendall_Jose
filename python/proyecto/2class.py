class Lampara:
    _ESTADO = ["ENCENDIDA", "APAGADO"]

    def __init__ (self, esta_encendida):
        self.esta_encendida = esta_encendida

    def muesta_lampara(self):
        if self.esta_encendida == True:
            print (self._ESTADO[0])
        else:
            print (self._ESTADO[1])

    def encender (self):
        self.esta_encendida = True
        self.muesta_lampara()

    def apagar (self):
        self.esta_encendida = False
        self.muesta_lampara()
    


def main ():

    lamp = Lampara(esta_encendida=False)
    
    while True :
        print ("Menú: n\ 0--> Apagar n\ 1--> Encender Lampara x-->Salir")

        op=input ("Que opción desea: ")
        if op == "0":
            lamp.apagar()
        elif op == "1":
            lamp.encender()
        else:
            break




if __name__== "__main__":
    main()