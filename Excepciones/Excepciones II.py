def divide():
#Concatenamos los except para recoger varios tipos de errores en un mismo Try.
	try: #Tiene que llevar un "except" o un "finally"
		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))
		print("El resultado de la división es: " + str(op1/op2))
	except ValueError:
		print("El valor introducido no es correcto.")
	except ZeroDivisionError:
		print("No se puede dividir entre cero.")
	except:
		# Esta forma de utilizar el except, recoge cualquier tipo de error.
		#   Por eso la respuesta puede ser general.
		print("Ha ocurrido un error") 
	#Lo que pongas dentro del finally se ejecuta siempre, tanto si ocurre una excepción como si no.
	#Suele utilizarse para cerrar bbdd
	#En el caso de no utilizar "except" y ocurrir un error, dierctamente se ejecuta
	#   lo que hay dentro del finally, y luego te muestra el tipo de error.
	finally:
		print("Cálculo finalizado.")

divide()