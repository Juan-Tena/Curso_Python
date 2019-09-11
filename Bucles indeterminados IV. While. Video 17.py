i=1

while i<=10:
	print("Ejecución " + str(i))
	i=i+1

print("Terminó la ejecución")


edad=int(input("Introduce la edad: "))
while edad<5 or edad>100:
	print("Has introducido una edad incorrecta. Vuleve a intentarlo.")
	edad=int(input("Introduce la edad: "))

print("Gracias por colaborar. Puedes pasar.")
print("Edad del aspirante: " + str(edad))

print("-------------------")

import math
print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número : "))

intentos=0

while numero<0:
	print("No se puede hallar la raíz cuadrada de un número negativo.")
	if intentos==2:
		print("Has consumido demasiados intentos. El programa ha finalizado.")
		break;
	numero=int(input("Introduce un número : "))
	if numero<0:
		intentos=intentos+1
if intentos <2:
	solucion=math.sqrt(numero) # Utilizamos la clase math
	print("La raíz cuadrada de " + str(numero) + " es: " + str(solucion) + ".")