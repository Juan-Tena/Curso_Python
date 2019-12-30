#Realización de pruebas con las funciones


#En este primer ejemplo, se realiza un solo test donde la función devuelve un string
def areaTriangulo(base, altura):

	"""
	Calcula el área de un triángulo dado.

	>>> areaTriangulo(3,6)
	'El área del triángulo es: 9.0'
	
	"""

	return "El área del triángulo es: " + str((base*altura)/2)

import doctest
doctest.testmod()

"""
Para probar la funcíón, tenemos que incluir >>>, el nombre de la función con datos de prueba, y 
a continuación, cual sería el resultado correcto.
Así mismo, deberemos importar el módulo doctest y escribirlo tal y como lo pone en las líneas
anteriores.
Si el resultado que proponemos es el que debería salir, no nos dirá nada. Pero si no coincide,
nos dará error.
"""

print(areaTriangulo(2,4))

print("==============================")


#En este segundo ejemplo, se realiza varios test donde la función devuelve un numérico
def areaTriangulo_1(base, altura):

	"""
	Calcula el área de un triángulo dado.

	>>> areaTriangulo_1(3,6)
	9.0

	>>> areaTriangulo_1(3,17)
	25.5

	>>> areaTriangulo_1(12,6)
	36.0
	
	"""
	return (base*altura)/2  #<--- en este caso, bastaría con poner debajo de >>> el número 9.0


import doctest
doctest.testmod()

print(areaTriangulo_1(5,8))


print("==============================")

#En este tercer ejemplo, se realizan varias comprobaciones
def compruebaMail(mailUsuario):
	"""
	La función compruebaMail, evalúa un mail recibido
	en busca de la @,
	Si tiene una @ es correcto, si tiene más de una @
	es incorrecto, y si tiene más de una @ es incorrecto.

	>>> compruebaMail('jbtena@gmail.com')
	True

	>>> compruebaMail('jbtenagmail.com@')
	False

	>>> compruebaMail('jbtena@gmail@com')
	False

	>>> compruebaMail('@jbtenagmail.com')
	False

	>>> compruebaMail('jbtenagmail.com')
	False

	"""
	arroba = mailUsuario.count('@') #Examinamos el mail recibido y contamos el número de @
	if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False
	else:
		return True


import doctest
doctest.testmod()