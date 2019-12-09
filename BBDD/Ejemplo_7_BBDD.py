#Realizamos operacones de tipo CRUD 
import sqlite3
#Conectamos, abrimos o creamos la bbdd
miConexion=sqlite3.connect("GestionProductos")
#Creamos el puntero o cursor
miCursor=miConexion.cursor()

#Realizamos un read (lectura)
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección'")
productos=miCursor.fetchall()
print(productos)

#Realizamos una actualización de un dato
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=34 WHERE NOMBRE_ARTICULO='Pelota'")

#Realizamos una eliminación de un registro
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")




miConexion.commit()

miConexion.close()