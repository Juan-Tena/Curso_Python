class Vehiculo():
	def __init__(self, marca, modelo): #Método constructor
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

class furgoneta(Vehiculo):
	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"



#Creamos un objeto de tipo moto que herede de la clase vehículos. Al crearla habrá heredado todas las propiedades
#  y todos los métodos de la clase vehiculos.
class Moto(Vehiculo): #Al poner dentro de los paréntesis la clase, le decimos que estamos heredando las propiedades y métodos de la clase vehiculos.
    # pass #permite no construir, de momento la clase.
    hcaballito=""
    def caballito(self):
    	self.hcaballito="Voy haciendo el caballito"    
    def estado(self): #Sobreescribimos el método estado, creado anteriormente, para poder mostrar el método "caballito" (sobreescritura de metodos)
    	print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha,
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)


class VElectricos(Vehiculo):
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia=100
	def cargarEnergia(self):
		self.cargando=True


