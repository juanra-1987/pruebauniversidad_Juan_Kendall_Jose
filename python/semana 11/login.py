from tkinter import *
from tkinter import ttk

def inicio():
    global root
    root = Tk()

    root.geometry("350x350")
    root.title("Ventan de Inicio")

    Label(root,text="Escoja una opción",bg="red").pack()
    Label(root,text="").pack()
    Button(root,text="Ir a login",width=30,font=("Arial Bold",14), height=3,bg="gray",command=Login).pack()
    Label(root,text="").pack()
    Button(root,text="Ir a registro",font=("Arial Bold",14),width=30, height=3,bg="gray",command=Registro).pack()

    root.mainloop()


def Login():
    ventana_login = Toplevel(root)
    ventana_login.title("Ventana Login")
    ventana_login.geometry("350x350")

    verificaUsuario= StringVar()
    verificaClave= StringVar()
    Label(ventana_login,text="Usuario:").pack()
    entradaUsuario = Entry (ventana_login,textvariable=verificaUsuario)
    entradaUsuario.pack()
    Label(ventana_login,text="Clave:").pack()
    entradaClave = Entry (ventana_login,textvariable=verificaClave,show="*")
    entradaClave.pack()
dic = {"Roll1":"Administrador",
        "Roll2":"Usuario",
        "Roll3":"Cajero"}
valores = []

for i,j in dic.items():
    valores.append(j)


def Registro():
    ventana_registro= Toplevel(root)
    ventana_registro.title("Ventana Registro")
    ventana_registro.geometry("350x350")
    usuarioRegistro= StringVar ()
    claveRegistro= StringVar ()
    rolcombo = StringVar()

    Label (ventana_registro, text="Por favor digite usuario").pack()
    entradausuarioRegistro=Entry (ventana_registro,textvariable=usuarioRegistro).pack()
    Label (ventana_registro, text="Por favor digite su clave").pack()
    entradaclaveRegistro=Entry (ventana_registro,textvariable=claveRegistro).pack()
    Label (ventana_registro, text="Elija un roll").pack()
    entradaclaveRegistro=Entry (ventana_registro,textvariable=claveRegistro).pack()


    comboboxRegistro = ttk.Combobox (ventana_registro, textvariable=rolcombo, values =valores).pack
    comboboxRegistro.pack()

    Button(ventana_registro,text="Guardar", command=GuardarRegistro)

usuario ={}

def GuardarRegistro():
    datos = []
    datos.append(claveRegistro.get())
    usuario[usuarioRegistro]


inicio()
