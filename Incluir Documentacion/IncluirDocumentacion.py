def areaCuadrado(lado):
	"""Calcula el área de un cuadrado
	elevando al cuadrado el lado pasado
	por parámetros."""
	
	#Esto es otro comentario, que no se imprimer por no estar entre las primeras comillas
	
	"""Este comentario, tempoco de imprime"""
	
	return "El área del cuadrado es: " + str(lado*lado)
	
	"""Esto también es un comentario, pero que no se imprime por no estar en las primeras comillas"""

def areaTriangulo(base, altura):
	"""Calcula el área de un triángulo
	utilizando los parámetros pasdos
	por parámetros."""

	return "El área del triángulo es: " + str((base*altura)/2)


print("1===========================")
print(areaCuadrado(5))

print("2===========================")
"""Con esta función le estamos diciendo que imprima
la documentación asociada a la función areaCuadrado"""
print(areaCuadrado.__doc__)

print("3===========================")
"""Con la función help(funcion), le pedimos que nos imprima
toda la información relativa a esta función"""
help(areaCuadrado)

print("4===========================")

print(areaTriangulo(5,6))

print("5===========================")

print(areaTriangulo.__doc__)

print("Clase====================================\n")

"""Si utilizamos una clase y dentro de ella escribimos funciones"""

class Areas:
	"""Esta es la ayuda general de la clase y que se imprime al escribir help(nombre de la clase).
	Esta clase calcula las áreas de diferentes figuras."""
	def areaCuadrado_1(lado):
		"""Calcula el área de un cuadrado
		elevando al cuadrado el lado pasado
		por parámetros."""
		
		#Esto es otro comentario, que no se imprimer por no estar entre las primeras comillas
		
		"""Este comentario, tempoco de imprime"""
		
		return "El área del cuadrado es: " + str(lado*lado)
		
		"""Esto también es un comentario, pero que no se imprime por no estar en las primeras comillas"""

	def areaTriangulo_1(base, altura):
		"""Calcula el área de un triángulo
		utilizando los parámetros pasdos
		por parámetros."""

		return "El área del triángulo es: " + str((base*altura)/2)

print("6===========================")
#En este caso, tenemos que incluir la clase a la que está vinculada la función, tal y como se ve a continuación.
help(Areas.areaCuadrado_1)

print("7===========================")
print(Areas.areaTriangulo_1.__doc__)

print("8===========================")
"""Si queremos obtener todas las ayudas que apoarecen en las funciones definidas dentro de una clase:"""
help(Areas)