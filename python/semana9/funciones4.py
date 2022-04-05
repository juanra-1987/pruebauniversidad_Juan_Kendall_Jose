import os
os.system("cls")

def validarCorreo(correoAvalidar):
    caracterEspecial ="@"
    for i in correoAvalidar:
        if i == caracterEspecial:
            return True
    return False



correo = input ("por favor digite su correo: ")
if validarCorreo(correo):
    print ("El correo es valido")
else:
    print ("El correo es invalido")