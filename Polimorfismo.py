class Coche():
	def desplazamiento(self):
		print("Me desplazo utilizando 4 ruedas")

class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando 2 ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")


#Para utilizar el médtodo desplazamiento, lo podemos hacer así, uno a uno, o...
#miVehiculo=Moto()
#miVehiculo.desplazamiento()

#miVehiculo2=Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3=Camion()
#miVehiculo3.desplazamiento()

#o lo podemos hacer de esta manera (polimorfismo):
def desplazamientovehiculo(vehiculo):#<--aquí tiene lugar el polimorfismo
	vehiculo.desplazamiento()


miVehiculo4=Camion()
desplazamientovehiculo(miVehiculo4)

miVehiculo5=Coche()
desplazamientovehiculo(miVehiculo5)