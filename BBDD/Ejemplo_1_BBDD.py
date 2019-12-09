##1 - Importamos la librería
import sqlite3

##2 - Abrir-Crear la conexión
##2.1 - Creamos la conexión
##Para crear la bbdd solo es necesario que exista el código de creación de la conexión y el código de cierre de la conexión (punto 7).
miConexion=sqlite3.connect("PrimeraBase")

##3 - Crear puntero o cursor
miCursor=miConexion.cursor()

##4 - Ejecutar query
##4.1 - Creamos la primera tabla
##Esta linea de creacion de la tabla, una vez ya creada, no debe de ejecutarse y por eso debe de aparecer comentada
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

##5 - Manejar los resultados
##Introducimos un solo dato en la bbdd
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15, 'DEPORTES')")

##Ahora utilizamos listas y tuplas para introducir varios datos. Lo que vamos a hacer, también se puede hacer con tres instrucciones INSERT INTO
#variosProductos=[
#	("Camiseta", 10, "Deporte"),
#	("Jarríon", 90, "Cerámica"),
#	("Camiseta", 20, "Juguetería")
#]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

##Ahora vamos a recuperar la información contenida en la bbdd
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall() #Lista que almacena los datos de la bbdd

print(variosProductos)
print("===============================")
for producto in variosProductos:
	print("Nombre del artículo:",producto[0], " - Sección:",producto[2]) #Al poner [0] nos extrae solo el nombre

##Esta instrucción lo que sirve es para confirmar los datos que hemos introducido
miConexion.commit()


##Cerrar puntero

##7 - Cerrar conexión
miConexion.close()