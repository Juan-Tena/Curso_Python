for i in ["Píldoras", "Informáticas",3]:
	print("Hola", end=" ") #Le decimos que no haya saltos de línea

print("--------------------")

for i in "jbtena@gmail.com": #En este caso el elemento a recorrer es un string, imprime tantas veces Hola como número de letras contenga la palabra
	print("Hola")

print("--------------------")

email=False

for i in "jbtena@gmail.com":
	if (i=="@"):
		email=True

if email==True:
	print("El e-mail es correcto")
else:
	print("El e-mail es incorrecto")

print("--------------------")

email=False
miemail=input("Introduce tu dirección de e-mail: ")
contador=0

for i in miemail:
	if (i=="@" or i=="."):
		contador=contador+1
if contador==2:		
		email=True

if email==True:
	print("El e-mail es correcto")
else:
	print("El e-mail es incorrecto")

print("--------------------")

for i in range(5):
	print("Hola")