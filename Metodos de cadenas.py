nombreusuario=input("Introduce un nombre de usuario: ")

#al ser un metodo, va despues del punto de la variable
print("el nombre es: ", nombreusuario.upper())
print("el nombre es: ", nombreusuario.lower())
print("el nombre es: ", nombreusuario.capitalize())

print("---------------------")

edad=input("Introduce la edad: ")
print(edad.isdigit())

while(edad.isdigit()==False):
	print("Por favor, introduce un valor numérico")
	edad=input("Introduce la edad otra vez: ")

if (int(edad)<18):
	print("No puede pasar")
else:
	print("Puede pasar")