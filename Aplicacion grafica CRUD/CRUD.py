from tkinter import *
from tkinter import messagebox
import sqlite3


root=Tk()

#=============Creamos la barra de menú===============
barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=300)

#Creamos los elementos de menu
bbddMenu=Menu(barramenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barramenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

crudMenu=Menu(barramenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barramenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

#Agregamos los elementos de menú a la barra de menú
barramenu.add_cascade(label="BBDD", menu=bbddMenu)
barramenu.add_cascade(label="Borrar", menu=borrarMenu)
barramenu.add_cascade(label="CRUD", menu=crudMenu)
barramenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#=========Comienzo de campos=================

#Frame de la parte superior
miFrame=Frame(root)
miFrame.pack()

cuadroID=Entry(miFrame)
cuadroID.grid(row=0,column=1, padx=10, pady=10) #el padx y el pady sirven para separar los Entry

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1,column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2,column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=3,column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=4,column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5,column=1, padx=10, pady=10)
#barras de desplazamiento del texto
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5,column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

root.mainloop()