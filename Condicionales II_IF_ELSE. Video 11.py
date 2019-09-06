
print("Verificación de acceso.")
edad_usuario=int(input("Introduce tu edad: "))
#
#if edad_usuario<18:
#	print("No puedes pasar. Lo siento.")
#else:
#	print("Puedes pasar.")
#print("El programa ha finalizado.")

# ¿Que hacemos si el usuario introduce una edad que no tiene sentido? Utilizamos "elif" 
if edad_usuario<18:
	print("No puedes pasar. Lo siento.")
elif edad_usuario>100:
	print("Edad incorrecta.")
else:
	print("Puedes pasar.")
print("El programa ha finalizado.")


# Otro ejemplo sería el siguiebte
print("Varificación de nota")
nota=int(input("Introduce la nota obtenida: "))