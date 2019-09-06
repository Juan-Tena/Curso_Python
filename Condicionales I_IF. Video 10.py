
#Flujo de ejecución de un programa y estructura condicional
# El flujo de ejecución de un programa es el orden con el que se ejecutan sus instrucciones.
# Las estructuras de tipo condicional pueden alterar el orden natural de arriba a abajo.

print("Programa de evaluación de notas")

nota_alumno=int(input("Introduce la nota del alumno: "))  #Cualquier número o texto que se introduzca a través de input(), python lo considera como texto.
                          #  por eso tenemos que utilizar la instrucción int, para convertir el texto en número.
def evaluacion(nota):
	valoracion="aprobado"   #La variable "valoracion" solo es accesible dentro del ámbito de la función
	if nota<5:
		valoracion="suspenso"
		calificacion=7 # En este caso, esta variable solo es accesible dentro del ámbito del IF.
	return valoracion

#print(evaluacion(7))
#print(evaluacion(4))

print(evaluacion(nota_alumno))
#La instrucción int(), también la podríamos introducir como "print(evaluacion(int(nota_alumno)))"
