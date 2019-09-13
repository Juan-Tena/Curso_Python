
#Los generadores son valores que se extraen de una función.
def generaPares(limite):
	num=1
	miLista=[]

	while num<=limite:
		miLista.append(num*2) #agrega un valor a la lista
		num=num+1
	return miLista

print(generaPares(10))

print("-------------------")

#Ahora utilizamos un generador

def generaPares1(limite):
	num=1

	while num<=limite:
		yield num*2
		num=num+1
devuelvePares=generaPares1(10)
for i in devuelvePares:
	print(i)

print("-------------------")

def generaPares2(limite):
	num=1

	while num<=limite:
		yield num*2
		num=num+1
devuelvePares=generaPares2(10)
print(next(devuelvePares))

print("Aquí prodría ir más código...")
print(next(devuelvePares))

print("Aquí prodría ir más código...")
print(next(devuelvePares))

print("-------------------")

def devuelve_ciudades(*ciudades): #Al colocarle el *, le indicamos a python que va a recibir un número indeterminado de elementos, y que los va ha recibir en forma de tupla.
	for elemento in ciudades:
		for subElemento in elemento: #Ahora queremos acceder a los subelementos de los elementos
			yield subElemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

print("Igual que antes pero con "+"yield from")

def devuelve_ciudades(*ciudades): #Al colocarle el *, le indicamos a python que va a recibir un número indeterminado de elementos, y que los va ha recibir en forma de tupla.
	for elemento in ciudades:
		yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))