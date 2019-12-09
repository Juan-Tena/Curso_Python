#Introducimos el concepto de la clausula UNIQUE 
import sqlite3
#Conectamos, abrimos o creamos la bbdd
miConexion=sqlite3.connect("GestionProductos")
#Creamos el puntero o cursor
miCursor=miConexion.cursor()
#Creamos la tabla y los campos que la forman
miCursor.execute(''' 
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
	PRECIO INTEGER, 
	SECCION VARCHAR(20))
''') #Se utiliza una triple coma cuando la instrucción es muy larga y quieres dividirla 
     #   en varios renglones.
#Especificamos los datos que vamos a introducir
productos=[
	("Pelota", 20, "Juguetería"),
	("Pantalón", 15, "Confección"),
	("Destornillado", 25, "Ferretería"),
	("Jarrón", 45, "Cerámica")	
]
#Introducimos los datos
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()