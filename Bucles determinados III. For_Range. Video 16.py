for i in range(5): #Aquí vamos desde el 0 hasta el 4
	print(i)
	 #Podemo unir texto con variable de manera sencilla
	print(f"valor de la variable {i}")

print("----------------------------")

#Nos permite contar desde el 5 hasta el 9
for j in range(5,10): #Desde un número inicial hasta un número final
	print(f"valor de la variable {j}")

print("----------------------------")

#Nos permite incrementar el conteo
for j in range(5,50,3): #Empieza en el 5, termina en el 49 y va de tres en tres. En este ejemplo, termina en el 47
	print(f"valor de la variable {j}")

print("----------------------------")

valido=False

email=input("Introduce tu e-mail: ")

for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido:
	print("E-mail correcto")
else:
	print("E-mail incorrecto")


