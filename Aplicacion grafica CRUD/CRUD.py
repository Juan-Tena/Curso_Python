from tkinter import *
from tkinter import messagebox
import sqlite3


#=================FUNCIONES=================

#Creamos la BBDD
def conexionBBDD():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	#Creamos una excepción para el caso de que la bbdd ya esté creada
	try:#Intenta crear la bbdd
		miCursor.execute(''' 
			CREATE TABLE DATOSUSUARIOS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50), 
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(10),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')
		messagebox.showinfo("BBDD", "Base de datos creada con éxito")
	except:#Mensaje que muestra en el caso de que la bbdd esté ya creada
		messagebox.showwarning("¿Atención", "La BBDD ya existe")


#Salir de la aplicación
def salirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
	if valor=="yes":
		root.destroy()#Me permite salir de la aplicación

#Borrar o resetear todos los campos label
def limpiarCampos():
	miId.set("")#De esta manera establecemos el valor a una cadena vacía
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	textoComentario.delete(1.0, END)

#CRUD - Crear
def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, '" + miNombre.get() + 
		"','" + miPass.get() + 
		"','" + miApellido.get() + 
		"','" + miDireccion.get() + 
		"','" + textoComentario.get("1.0",END) + "')")
	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro insertado con éxito")

#CRUD: permite leer el contenido de la bbdd
def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()	
	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" +miId.get())
	elUsuario=miCursor.fetchall()# La función fetchall nos devuelve
	      # un array con los registros que contiene la bbdd
	for usuario in elUsuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComentario.insert(1.0, usuario[5])
	miConexion.commit()

#CRUD: permite actualizar el contenido de la bbdd
def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()	
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', PASSWORD='" + miPass.get() + 
		"', APELLIDO='" + miApellido.get() +
		"', DIRECCION='" + miDireccion.get() +
		"', COMENTARIOS='" + textoComentario.get(1.0, END) +
		"' WHERE ID=" + miId.get()) 
	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro actualizado con éxito")










root=Tk()
#=============CREACIÓN DE LA BARRA DE MENÚ===============
barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=300)

#Creamos los elementos de menu
bbddMenu=Menu(barramenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barramenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barramenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barramenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

#Agregamos los elementos de menú a la barra de menú
barramenu.add_cascade(label="BBDD", menu=bbddMenu)
barramenu.add_cascade(label="Borrar", menu=borrarMenu)
barramenu.add_cascade(label="CRUD", menu=crudMenu)
barramenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#==================CREACIÓN DE LOS FRAME'S===================

#Frame de la parte superior
miFrame=Frame(root)
miFrame.pack()

#Creamos las variables de control: objetos especiales que se asocian a los 
#        widgets para almacenar sus valores y facilitar su disponibilidad en otras partes del programa
#Estas variable me permiten decir a la aplicación que va a haber una cadena de caracteres
miId=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()

#Creamos los elementos del frame
cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0,column=1, padx=10, pady=10) #el padx y el pady sirven para separar los Entry

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1,column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2,column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3,column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5,column=1, padx=10, pady=10)
#barras de desplazamiento vertical del texto
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5,column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#Creamos ahora los label del frame superior

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

NombreLabel=Label(miFrame, text="Nombre:")
NombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)


#Frame de la parte inferior (botones)

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar")
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)








root.mainloop()