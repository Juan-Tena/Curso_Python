# Los decoradores son funciones que añaden funcionalidades a funciones que ya existen
#   en el programa.

#Una función decorador está formada por 3 funciones.
#Un decorador devuelve una función.

"""Estructura de una función decorador:
def función_decorador(función): <---Función A
	def funcion_internal(): <--- Función B
		código de la fución interna
	return función_interna <--Funcion C
"""

#EJEMPLO: Supongamos que a las funciones suma() y resta(), le queremos añadir la misma funcionalidad.
#En lugar de ir una a una y modificarlas, utilizamos una función decoradora y que situaremos
#   al inicio del programa.

def funcion_decoradora(funcion_parametro):
	def funcion_interior():
		#Acciones iniciales adicionales que decoran
		print("Vamos a realizar un cálculo: ")
		funcion_parametro()
		#Acciones posterioes adicionales que decoran
		print("Hemos terminado el cálculo")
	return funcion_interior

#Agregamos esta expresión junto con la función, para que la fución decoradora se ejecute.
@funcion_decoradora
def suma():
	print(15+20)
#En este caso no se ejecuta la función decoradora
def resta():
	print(30-10)

@funcion_decoradora
def resta_1():
	print("Esto es una resta:", 50-25)


suma()
print("================")
resta()
print("================")
resta_1()

print("=====================================================================")