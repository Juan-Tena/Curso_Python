class Coche(): #creamos la clase
	#Definimos las propiedades de la clase coche
	
	def __init__(self): #creamos el método constructor
		#Especificamos un estado inicial
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 #encapsulamos la variable poniendo dos guiones delante de la variable 	para que no pueda ser modificada. 
							#No es aceesible desde fuera de la clase, pero si desde dentro de la clase.
		self.__enmarcha=False
	
	#Creamos los métodos o comportamientos
	def arrancar(self, arrancamos):
		self.__enmarcha=arrancamos
		if(self.__enmarcha):
			chequeo=self.__chequeo_interno


		if(self.__enmarcha and chequeo):
			return "El coche está en marcha"
		elif(self.__enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo. No podemos arrancar."
		else:
			return "El coche está parado"


	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

#Encapsulamos este método para que solo pueda ser llamado desdo otro método de 
#   dentro de la clase (le ponemos dos guiones delante del nombre)		
	def __chequeo_interno(self):
		print("Realizando chequeo interno.")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False



#Creamos una instancia (instanciar una clase)
miCoche=Coche()
#print("El largo del coche es: ", miCoche.largoChasis)
#print("El coche tiene ", miCoche.ruedas, " ruedas")
print(miCoche.arrancar(True))
miCoche.estado()
#print(miCoche.chequeo_interno())

print("............A continuación creamos el segundo objeto..............")

miCoche2=Coche()
#print("El largo del coche2 es: ", miCoche2.largoChasis)
#print("El coche2 tiene ", miCoche2.ruedas, " ruedas")
print(miCoche2.arrancar(False))
miCoche2.__ruedas=2 #Modificamos el estado de la propiedad, pero como está encapsulada, no tiene efecto. 
miCoche2.__anchoChasis=2000
miCoche2.estado()
print(miCoche2.__chequeo_interno())
