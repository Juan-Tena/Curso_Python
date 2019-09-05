#Creación de una tupla
mitupla=("Juan", 13 , 1, 1995, "Juan")

#Acceder a un elemento de la tupla
print(mitupla[2])

#Hay dos métodos que permiten convertir tuplas en listas y al revés
milista=list(mitupla) #Convierte una tupla en una lista
print(milista) #Sabemos que es una lista porque imprme los datos entre corchetes
print(mitupla) #Sabemos que es una tupla porque imprme los datos entre paréntesis


mitupla2=tuple(milista) #Convierte una lista en una tupla
print(mitupla2) #Sabemos que es una tupla porque imprme los datos entre paréntesis


#Para8 acceder a un elemento de la tupla
print("Juan" in mitupla) #Me contesta True o False según si lo encuentra en la tupla o no lo encuentra
print("pepe" in mitupla)

#Para averiguar el número de veces que un elemento existe en una determianda tupla
print(mitupla.count("Juan"))

#Podemos averiguar la longitud de una tupla
print(len(mitupla))

#Creación de tuplas unitarias, es decir, tuplas con un único elemento
mitupla3=("Juan",)
print(len(mitupla3))

#Creación de una tupla de manera alternativa, sin paréntesis. Se conoce como "Empaquetado de tupla"
mitupla4 = "Juan",13,1,1995
print(mitupla4)

#Desempaquetado de tupla: permite asignar todos los elementos que forman parte de una tupla, a diferentes 
#	variables de una manera sencilla
nombre, dia,mes, agno=mitupla4
print(nombre)
print(dia)
print(agno)
print(mes)

#Las tuplas no se pueden modificar, ni añadir ningún elemento adicional
mitupla4.append("Paco")