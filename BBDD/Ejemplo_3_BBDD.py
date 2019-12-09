#Introducimos el concepto de campo clave en la bbdd
import sqlite3
#Conectamos, abrimos o creamos la bbdd
miConexion=sqlite3.connect("GestionProductos")
#Creamos el puntero o cursor
miCursor=miConexion.cursor()

#Introducimos un dato nuevo
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','Tren',15,'Juguetería')")

#Si tratamos de introducir este registro, nos dará un error de tipo UNIQUE, dado que AR03 ya existe previamente
miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR03','Tren',15,'Juguetería')")

miConexion.commit()

miConexion.close()