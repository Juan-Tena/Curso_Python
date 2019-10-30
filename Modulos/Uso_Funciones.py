
##Esta es la versión larga e incómoda
##Importamos el modulo
#import Funciones_Matematicas
##y lo llamamos para utilizar las funciones
#Funciones_Matematicas.sumar(2,5)
#Funciones_Matematicas.restar(2,5)

##Esta otra forma es más cómoda
#from Funciones_Matematicas import sumar
#sumar(5,7)
##En este caso, si queremos utilizar otra función hay que invocarla
#from Funciones_Matematicas import restar
#restar(12,7)

from Funciones_Matematicas import * #El problema aquí es que estás utilizando mucha memoria
sumar(5,7)
restar(12,7)
multiplicar(7,5)