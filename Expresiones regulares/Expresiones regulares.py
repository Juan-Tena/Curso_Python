import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

print(re.search("aprender", cadena)) # Texto que vamos buscando, texto donde lo queremos buscar 
#La ejecución nos devuelve un objeto sre.SRE_Match y nos dice si ha encontrado la frase
print("1=====================================")

#Si no encuentra la palabra, devuelve None
print(re.search("aprenderrrr", cadena))
print("2=====================================")

textoBuscar = "aprender"

if(re.search(textoBuscar, cadena)) is not None:
	print("He encontradao el texto")
else:
	print("No he encontradao el texto")

print("3=====================================")
#Si queremos saber el caracter donde comienza el texto buscado dentro
#  de la cadena
textoEncontrado = re.search(textoBuscar, cadena)
print(textoEncontrado.start())

print("4=====================================")
#Si queremos saber el caracter donde termina el texto buscado dentro
#  de la cadena
print(textoEncontrado.end())

print("5=====================================")
#Si queremos saber el caracter donde empieza y termina el texto buscado dentro
#  de la cadena
#Devuelve los valores en una tupla
print(textoEncontrado.span())

print("6=====================================")
#E este caso, el texo se encuentra dos veces
textoBuscar1 = "Python"
print(re.search(textoBuscar1, cadena))
#En este caso, solo muestra la primera coincidencia. Si queremos que muestre todas:
print(len(re.findall(textoBuscar1, cadena)))
print("7=====================================")


#Vamos a ver las ANCLAS: comienzo y fin
lista_nombres = ['Ana Gómez',
'María Martín',
'Sandra López',
'Santiago Martín',
'Sandra Altozano']
#el metacaracter ^ lo que hace es buscar todos los registros y comprobar cual comienza por Sandra
for elemento in lista_nombres:
	if re.findall('^Sandra', elemento):
		print(elemento)

print("8=====================================")
#el metacaracter $ lo que hace es buscar todos los registros y comprobar cual termina por Maertín
for elemento1 in lista_nombres:
	if re.findall('Martín$', elemento1):
		print(elemento1)

print("9=====================================")
lista_nombres1 = ['http://pildorasinformaticas.com',
'ftp://pildorasinformaticas.com',
'http://pildorasinformaticas.es',
'ftp://pildorasinformaticas.es']

for elemento1 in lista_nombres1:
	if re.findall('.es$', elemento1):
		print(elemento1)
print("10====================================")
for elemento1 in lista_nombres1:
	if re.findall('^ftp', elemento1):
		print(elemento1)		

print("11====================================")

#Vamos a ver los CLASES DE CARACTERES
lista_nombres = ['http://www.informaticaenespaña.es',
'http://pildorasinformaticas.es',
'http://pildorasinformaticas.com']

#Buscamos en cualquier parte de la lista, si hay algún registro que contiene la letra ñ.
for elemento in lista_nombres:
	if re.findall('[ñ]', elemento):
		print(elemento)

print("12====================================")
lista_nombres = ['hombres',
'mujeres','mascotas', 'niños', 'niñas']

#Buscamos en cualquier parte de la lista, si hay más de un registro que contiene la letra ñ.
for elemento in lista_nombres:
	if re.findall('niñ[oa]s', elemento):
		print(elemento)

print("13====================================")
lista_nombres = ['hombres',
'mujeres','mascotas', 'camión', 'camion']

#Buscamos en cualquier parte de la lista, si hay más de un registro que contiene la letra ñ.
for elemento in lista_nombres:
	if re.findall('cami[óo]n', elemento):
		print(elemento)

print("14====================================")

#Vamos a trabajar con RANGOS

lista_nombres = ['Ana', 'Pedro', 'María', 'Rosa', 'Sandra', 'Celia', 'Aulelio']
#Buscamos las palabras en una lista que contengan las letras contenidas 
# en un determinado rango
for elemento in lista_nombres:
	if re.findall('[o-t]', elemento):
		print(elemento)
print("15====================================")
#En este caso debería devolver todos los registros que comiencen por el rango
# teniendo en cuenta que distingue entre mayúsculas y minúsculas
for elemento in lista_nombres:
	if re.findall('^[o-t]', elemento):
		print(elemento)
print("16====================================")
for elemento in lista_nombres:
	if re.findall('[O-T]', elemento):
		print(elemento)
print("17====================================")
for elemento in lista_nombres:
	if re.findall('[o-t]$', elemento):
		print(elemento)
print("18====================================")

lista_nombres = ['Ma1', 'Se1', 'Ma2', 'Ba1', 'Ma3', 'Va1', 'Va2', 'Ma4']
for elemento in lista_nombres:
	if re.findall('Ma[0-3]$', elemento):
		print(elemento)
print("19====================================")
#Rango negado: buscamos que nos devuelva los valores que no están comprendidos
# en el rango
for elemento in lista_nombres:
	if re.findall('Ma[^0-3]', elemento):
		print(elemento)
print("20====================================")
lista_nombres = ['Ma1', 'Se1', 'Ma2', 'Ba1', 'Ma3', 'Va1', 'Va2', 'Ma4', 'MaA', 'Ma5', 'MaB', 'MaC']
for elemento in lista_nombres:
	if re.findall('Ma[0-3,A-B]', elemento):
		print(elemento)
print("21====================================")
lista_nombres = ['Ma.1', 'Se1', 'Ma2', 'Ba1', 'Ma:3', 'Va,1', 'Va2', 'Ma4', 'MaA', 'Ma.5', 'MaB', 'Ma;C']
for elemento in lista_nombres:
	if re.findall('[.,:]', elemento):
		print(elemento)

print("22====================================")
#Vamos a ver las funciones MATCH y SEARCH

nombre1 = "Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "María López"

#La función MATCH lo que hace es buscar si hay coincidencias en un patrón de 
#  búsquedas al comienzo de una cadena de texto.

if re.match("Sandra", nombre1):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")
print("23====================================")
if re.match("Sandra", nombre2):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")
print("24====================================")

nombre1 = "Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "sandra López"
#Distingue entre mayúsculas y minúsculas
if re.match("Sandra", nombre3):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

print("25====================================")

#Si queremos que la función MATCH no haga este tipo de distinción
#  entre mayúsculas y minúsculas
if re.match("Sandra", nombre3, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

print("26====================================")
nombre1 = "Jara López"
nombre2 = "Antonio Gómez"
nombre3 = "Lara López"

if re.match(".ara", nombre1, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

if re.match(".ara", nombre2, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

if re.match(".ara", nombre3, re.IGNORECASE):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

print("27====================================")

#Vamos abuscar cadena que comiencen por números
cadena1 = "Jara López"
cadena2 = "45345435435"
cadena3 = "a2424324"

if re.match("\d", cadena1):
	print("Hemos encontrado el número")
else:
	print("No lo hemos encontrado")

if re.match("\d", cadena2):
	print("Hemos encontrado el número")
else:
	print("No lo hemos encontrado")

if re.match("\d", cadena3):
	print("Hemos encontrado el número")
else:
	print("No lo hemos encontrado")

print("28====================================")
#La función SEARCH busca en toda la cadena, y al contrario que la función MATCH, que busca al principio
#   de la cadena.
nombre1 = "Jara López"
nombre2 = "Antonio Gómez"
nombre3 = "Lara López"

if re.search("López", nombre1):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

if re.search("López", nombre2):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

if re.search("López", nombre3):
	print("Hemos encontrado el nombre")
else:
	print("No lo hemos encontrado")

print("29====================================")
codigo1 = "fdsfdsfdsfdsfdfdfdsfdfd71dfgfdgfg"
codigo2 = "gsfsdf71dbbdfgfdgfdgfdgfdgfdggfgfdfdgg"
codigo3 = "hjghjkukyuttgdbthytjh"

if re.search("71", codigo1):
	print("Hemos encontrado el número")
else:
	print("No lo hemos encontrado")

if re.search("71", codigo2):
	print("Hemos encontrado el número")
else:
	print("No lo hemos encontrado")

if re.search("71", codigo3):
	print("Hemos encontrado el número")
else:
	print("No lo hemos encontrado")
