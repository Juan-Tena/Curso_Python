
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
devulvePares=generaPares1(10)
for i in devulvePares:
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