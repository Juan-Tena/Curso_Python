
#Al crear un diccionario, debemos establecer la estructura de clave-valor
#Creamos un diccionario que almacena paises y diccionarios
midiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}

#Accedemos a un elemento concreto del diccionario preguntando a la clave
print(midiccionario["Francia"])
print(midiccionario["España"])

#Si queremos acceder a un diccionario entero
print(midiccionario)

#Agregamos más elementos a un diccionario ya creado
midiccionario["Italia"]="Lisboa"
print(midiccionario)

#Modificamos el valor de una clave: sobrescribimos el valor de la clave
midiccionario["Italia"]="Roma"
print(midiccionario)

#Eliminamos un elemento del diccionario
del midiccionario["Reino Unido"]
print(midiccionario)

#Diccionario con varios tipos de datos
midiccionario1={"Alemania":"Berlín", 23:"Jordan", "Mosqueteros":3}
print(midiccionario1)

#Utilizamos una tupla para asignar las claves a cada uno de los valores 
mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario2={mitupla[0]:"Madrid", mitupla[1]:"París", mitupla[2]:"Londres", mitupla[3]:"Berlín"}
print(midiccionario2)
print(midiccionario2["Francia"])

#Como hacemos para que un diccionario almacene una tupla
midiccionario3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos": [1991, 1992, 1993, 1996, 1997, 1998]}
print(midiccionario3)
print(midiccionario3["Equipo"])
print(midiccionario3["anillos"])

#Guardamos un diccionario dentro de otro diccionario
midiccionario4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos": {"Temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(midiccionario4["anillos"])
print(midiccionario4)

print(midiccionario4.keys())
print(midiccionario4.values())
print(len(midiccionario4))