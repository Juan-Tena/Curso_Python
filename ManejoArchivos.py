#Importamos el modulo io, y dentro de él em método open
from io import open

#Creamos un archivo con permisos de escritura 
archivo_texto=open("archivo.txt", "w")

frase="Estupendo día para estudiar Python \nel mércoles"

archivo_texto.write(frase) #Escribimos lo que queramos en el fichero

archivo_texto.close()

#Abrimos el fichero en modo lectura.
archivo_texto1=open("archivo.txt", "r") 

texto=archivo_texto1.read()

print("En el fichero pone: ", texto)

archivo_texto1.close()

print("1----------------------------")

#abrimos el archivo en modo lectura
archivo_texto2=open("archivo.txt", "r") 

#├Se almacena en cada línea de texto en un elemento de lista
lineas_texto=archivo_texto2.readlines()

archivo_texto2.close()

print(lineas_texto[0])
print(lineas_texto[1])

print("2----------------------------")

#abrimos el archivo en modo append, lo que nos permitirá añadir datos
archivo_texto3=open("archivo.txt", "a")
archivo_texto3.write("\nlo cual siempre es una buena ocasión para estudiar python")
archivo_texto3.close()

print("3----------------------------")

archivo_texto3=open("archivo.txt", "r")
print("1",archivo_texto3.read()) #Una vez lee el fichero, situa el cursor al final.
#En esta segunda línea no lee nada porque el puntero se situa al final despues del primer read
#   y no encuentra nada
print("2",archivo_texto3.read())

#¿Cómo podemos modificar la posición del puntero?
archivo_texto3.seek(10)
print("3",archivo_texto3.read())

archivo_texto3.seek(0)
print("4",archivo_texto3.read())

archivo_texto3.close()

#Otra manera de acceder a los datos es con read.
#En este caso, se trata de una lectura "hasta"
archivo_texto4=open("archivo.txt", "r")
print("5",archivo_texto4.read(11))
#Esta segunda lectura se realiza a partir de donde se queda el puntero
print("6",archivo_texto4.read())

archivo_texto4.close()

print("4----------------------------")

archivo_texto5=open("archivo.txt", "r")

archivo_texto5.seek(len(archivo_texto5.read())/2)
print(archivo_texto5.read())

archivo_texto5.close()

print("5----------------------------")

archivo_texto6=open("archivo.txt", "r+")#Le decismos que abrimos el fichero en modo lectura y escritura
archivo_texto6.write("Comienzo del texto")

#print(archivo_texto6.readlines())

lista_texto=archivo_texto6.readlines() 
lista_texto[1]="Esta linea ha sido incluida desde el exterior \n"
archivo_texto6.seek(0)
archivo_texto6.writelines(lista_texto)

archivo_texto6.close()