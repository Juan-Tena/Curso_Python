milista=["María","Pepe","Marta","Antonio"]

#De esta menra listo todos los componentes de la lista
print(milista[:]) 

 #Solo listo el componente que ocupa el ídice 2 de la lista. Recordar que se empieze por 0.
print(milista[2])

#Se genera un error porque este índice no existe
#print(milista[5]) 

#AAl introducir un índice con signo negativo, cuenta desde el final
#  aunque en este caso,empieza a contar desde -1.
print(milista[-2])

#Porción de lista: cuando queremos accceder solo a una parte de la lista
print(milista[0:3]) #Se seleccionan los 3 primeros y se empieza por el 0
print(milista[2:3]) #Se seleccionan los 3 primeros y se empieza por el 2
print(milista[:2])
print(milista[1:2])
print(milista[2:]) #Accedemos a los dos últimos elementos

#Para agregar elementos a una lista
milista.append("Sandra") #Agrega el elemento al final de la lista
print(milista[:])
milista.insert(2,"Elena") #Agregamos en el índice 2 este elemento
print(milista[:])

#Para agregar varios elementos a la lista
milista.extend(["Felipe","Ana","Lucia"])
print(milista[:])

#Nos devuelve el índice de un elemento
print(milista.index("Antonio"))
print(milista.index("Ana"))

#¿Que pasa cuando hay dos nombre iguales
milista.append("Elena")
print(milista[:])
print(milista.index("Elena"))

#Comprobamos si una elemento se encuentra en una lista
print("María" in milista)

#También se pueden eliminar elementos
milista.remove("Ana")
print(milista[:])

#También podemos elminar el último elemento de una lista
milista.pop()
print(milista[:])

#Una lista puede contener cualquier tipo de elementos
milista1=["María", 5, True, 78.35]
print(milista1[:])

#Unir listas
milista2=milista+milista1
print(milista2[:])

#Operador multiplicador: repite las listas
milista3=["María", 5, True, 78.35]*3
print(milista3[:])


