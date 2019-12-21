

#Las funciones lambda son funciones anónimas, y se utilizan para hacer que la sintaxis sea más ligera y para ahorrarnos tiempo
"""def  area_triangulo(base, altura):
	return (base*altura)/2

#Supongamos que esta función se va a utilizar repetidamente
print(area_triangulo(5,7))

triangulo_1=area_triangulo(5,7)
triangulo_2=area_triangulo(9,6)

print(triangulo_1)
print(triangulo_2)"""

area_triangulo=lambda base,altura:(base*altura)/2
print(area_triangulo(5,7))

al_cubo=lambda numero:pow(numero,3)
al_cubo_1=lambda numero:numero**3

print(al_cubo(5))
print(al_cubo_1(15))


destacar_valor=lambda comision: "¡{}! euros".format(comision)
comision_Ana=15585

print(destacar_valor(comision_Ana))