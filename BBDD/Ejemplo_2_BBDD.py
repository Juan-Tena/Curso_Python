#Introducimos el concepto de campo clave en la bbdd
import sqlite3
#Conectamos, abrimos o creamos la bbdd
miConexion=sqlite3.connect("GestionProductos")
#Creamos el puntero o cursor
miCursor=miConexion.cursor()
#Creamos la tabla y los campos que la forman
miCursor.execute(''' 
	CREATE TABLE PRODUCTOS (
	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
	NOMBRE_ARTICULO VARCHAR(50), 
	PRECIO INTEGER, 
	SECCION VARCHAR(20))
''') #Se utiliza una triple coma cuando la instrucción es muy larga y quieres dividirla 
     #   en varios renglones.
#Especificamos los datos que vamos a introducir
productos=[
	("AR01", "Pelota", 20, "Juguetería"),
	("AR02","Pantalón", 15, "Confección"),
	("AR03","Destornillado", 25, "Ferretería"),
	("AR04","Jarrón", 45, "Cerámica")	
]
#Introducimos los datos
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

miConexion.commit()

miConexion.close()