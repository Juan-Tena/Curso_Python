#1 - Importamos la librería
import sqlite3

#2 - Abrir-Crear la conexión
#2.1 - Creamos la conexión
#Para crear la bbdd solo es necesario que exista el código de creación de la conexión y el código de 
#  cierre de la conexión (punto 7)
miConexion=sqlite3.connect("PrimeraBase")

#3 - Crear puntero o cursor
miCursor=miConexion.cursor()

#4 - Ejecutar query
#4.1 - Creamos la primera tabla
#Esta linea de creacion de la tabla, una vez ya creada, no debe de ejecutarse y por eso debe de aparecer comentada
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#5 - Manejar los resultados
#Introducimos datos en la bbdd
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15, 'DEPORTES')")
miConexion.commit() #Esta instrucción lo que sirve es para confirmar los datos que hemos introducido



#Cerrar puntero

#7 - Cerrar conexión
miConexion.close()