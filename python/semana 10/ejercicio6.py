from tkinter import Button, messagebox
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x400")

def llamar ():
    messagebox.showinfo(message="Hola este es el mensaje", title="Este es el titulo")

Button (ventana,text="click aquí",command=llamar).pack()

ventana.mainloop()