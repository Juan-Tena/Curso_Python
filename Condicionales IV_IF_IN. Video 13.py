print("Asignaturas optativas año 2019")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")

opcion=input("Escribe la asignatura escogida : ")
asignatura=opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida " + asignatura)
else:
	print("La asignatura escogida no está contemplada")