#Importamos el modulo io, y dentro de él em método open
from io import open

#Creamos un archivo con permisos de escritura 
archivo_texto=open("archivo.txt", "w")

frase="Estupendo día para estudiar Python \nel mércoles"

archivo_texto.write(frase) #├Escribimos lo que queramos en el fichero

archivo_texto.close()

#Abrimos el fichero en modo lectura.
archivo_texto1=open("archivo.txt", "r") 

texto=archivo_texto1.read()

print("En el fichero pone: ", texto)

archivo_texto1.close()

print("----------------------------")

#abrimos el archivo en modo lectura
archivo_texto2=open("archivo.txt", "r") 

#├Se almacena en cada línea de texto en un elemento de lista
lineas_texto=archivo_texto2.readlines()

archivo_texto2.close()

print(lineas_texto[0])
print(lineas_texto[1])

print("----------------------------")

#abrimos el archivo en modo append, lo que nos permitirá añadir datos
archivo_texto3=open("archivo.txt", "a")
archivo_texto3.write("\nlo cual siempre es una buena ocasión para estudiar python")
archivo_texto3.close()
