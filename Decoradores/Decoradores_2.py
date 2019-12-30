#En el ejemplo del fichero Decoradores_1.py hemos visto que las funciones no reciben parámetros.
#   En este segundo ejemplo, vamos a añador los parámetros en las funciones.

def funcion_decoradora(funcion_parametro):
	def funcion_interior(*args, **kwards): #<-, --le decimos a una función que va a recibir un número indeterminado de parámetros y de argumentos con clave
		#Acciones iniciales adicionales que decoran
		print("Vamos a realizar un cálculo: ")
		funcion_parametro(*args, **kwards)#<-- también aquí le indicamos que vamos a recibir parámetros
		#Acciones posterioes adicionales que decoran
		print("Hemos terminado el cálculo")
	return funcion_interior

#Agregamos esta expresión junto con la función, para que la fución decoradora se ejecute.
@funcion_decoradora
def suma(num1, num2, num3):
	print(num1 + num2 + num3)
#En este caso no se ejecuta la función decoradora

@funcion_decoradora
def resta(num1, num2):
	print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
	print(pow(base, exponente))


suma(7,5,8)
print("================")
resta(12,10)
print("================")
#En este caso, al haber añadido "**kwards", la función decoradora funciona.
#  Si la función decoradora no llevase "**kwards", el utilizar la función con claves (base= y exponente=) no funcionaría y daría error
potencia(base=5,exponente=5)

print("=====================================================================")