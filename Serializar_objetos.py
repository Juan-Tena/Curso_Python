import pickle

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

coche1=Vehiculo("Mazda","MX5")
coche2=Vehiculo("SEAT","Leon")
coche3=Vehiculo("Renault","Megane")

#Serializamos los coches
coches=[coche1, coche2, coche3]

fichero=open("losCoches", "wb")
pickle.dump(coches,fichero)
fichero.close()

del (fichero)

ficheroApertura=open("losCoches","rb")

misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
	print(c.estado())