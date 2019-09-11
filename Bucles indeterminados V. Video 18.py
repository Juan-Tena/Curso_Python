for letra in "Python":

	if letra=="h":
		continue #Lo que hace es saltar el código posterior del bucle

	print("Viendo la letra : " + letra)

print("--------------------")

nombre="Píldoras informáticas"
contador=0

for i in nombre:
	if i==" ":
		continue #L está diciendo que ignore lo que hay a continuación del bucle, y realice la siguiente iteración.
	contador+=1

print(contador)

print("--------------------")

#while True:
#	pass #Esto lo que hace es mantener el programa hasta que se pulsa Ctrl+c

print("--------------------")

email=input("Introduce tu e-mail : ")

for i in email:
	if i=="@":
		arroba=True
		break;
else:
	arroba=False

print(arroba)