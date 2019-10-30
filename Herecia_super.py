class Persona():
	def __init__(self, nombre, edad, lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia
	def descripcion(self):
		print("Nombre:", self.nombre, "; Edad:", self.edad, "; Residencia:", self.lugar_residencia)

juan=Persona("Juan", "51", "Valencia")
juan.descripcion()
print("---------------------------")

class Empleado(Persona):
	
	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #Llamamos al constructor de la clase padre, para que al instaciar
		         # una clase, podamos inotroducir los valores de los argumentos de la clase superior
		self.salario=salario
		self.antigüedad=antigüedad
	
	def descripcion(self):
		super().descripcion() #llamamos al método de la clase superior.
		print("Salario:", self.salario, "Antigüedad:", self.antigüedad)




amparo=Empleado(25000,5, "Antonio", 55, "España")
print("Amparo gana", amparo.salario)
print("---------------------------")
#amparo.nombre="amparo"
#amparo.edad=33
#amparo.lugar_residencia="Madrid"
amparo.descripcion()
print("---------------------------")

# Principio de sustitución
print(isinstance(amparo, Empleado))
print(isinstance(amparo, Persona))

manuel=Persona("Manuel", 55, "España")
print(isinstance(manuel, Persona))
print(isinstance(manuel, Empleado))