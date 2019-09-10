
print("Programa de becas año 2019")

distancia_escuela=int(input("Introduce la distancia a la escuela en km : "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el número de hermanos en el centro : "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario familiar anual bruto : "))
print(salario_familiar)


if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
 	print("Tienes derecho a beca de tipo 1")
else:
	print("No tienes derecho a beca de tipo 1")

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
 	print("Tienes derecho a beca de tipo 2")
else:
	print("No tienes derecho a beca de tipo 2")