

#Esta función, lo que hace es aplicar una función a cada elemento de una lisa iterable
#    (listas, tuplas, etc), devolviendo una lista con los resultados.

class Empleado:
	def __init__(self,nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
	def __str__(self):
		return "{} que trabaja como {} y tiene un salario de {} euros".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
Empleado("Juan", "Director",7500),
Empleado("Ana", "Presidenta",8500),
Empleado("Alba", "Administrativo",2500),
Empleado("Amparo", "Secretaria",2700),
Empleado("Antonio", "Botones",1500),
]
#Calcula la comisión para todos los salarios
def calculo_comision(empleado):
	empleado.salario=empleado.salario*1.03
	return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
	print(empleado)

print("==============================\n")

#Calcula la comisión solo para aquellos que cumplan una determinada
#   condición: salario <=3000
def calculo_comision1(empleado):
	if(empleado.salario<=3000):
		empleado.salario=empleado.salario*1.03
	return empleado

listaEmpleadosComision=map(calculo_comision1, listaEmpleados)

for empleado in listaEmpleadosComision:
	print(empleado)