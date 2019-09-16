def evaluaEdad(edad):
	if edad<0:
		#Podemos personalizar el mensaje
		raise TypeError("No se permiten edades negativas")
	#	raise ZeroDivisionError("No se permiten edades negativas")	
	#	Una vez se produce el error, la ejecución se corta y no se ejecuta
	#		ningún código como en el caso de "except" o de "finally"

	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "Cuídate..."

print(evaluaEdad(-18))