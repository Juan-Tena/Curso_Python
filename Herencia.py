class Vehiculo():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False #cuando construimos un vehículo, no está en marcha
		self.acelera=False #cuando construimos un vehículo no está en acelerando
		self.frena=False
	#Definimos los comportamientos del vehículo
	def arrancar(self):
		self.enmarcha=True
	def acelerar(self):
		self.acelera=True
	def frenar(self):
		self.frena=True
	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha,
				"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

#Creamos un objeto de tipo motocicleta que herede de la clase vehículos. Al crearla habrá heredado todas las propiedades
#  y todos los métodos de la clase vehiculos.
class Moto(Vehiculo): #Al poner dentro de los paréntesis la clase, le decimos que estamos heredando las propiedades y métodos de la clase vehiculos.
    pass #permite no construir, de momento la clase.

miMoto=Moto("Honda", "CBR")

#Creamos una instancia a la clase Moto miMoto=Moto("Honda", "CBR")

miMoto.estado()
miMoto.frenar()
print("--------------------")
miMoto.estado()
