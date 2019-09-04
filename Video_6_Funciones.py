def suma():
	num1=5
	num2=7
	print(num1+num2)

suma()
suma()
suma()

def suma1(num3,num4):
	print(num3+num4)

suma1(2,3)
suma1(5,7)
suma1(35,358)
#Los argumentos de una función pueden ser de varios tipos.

def suma2(num5,num6): #En este caso, el resultado no se visualiza 
	resultado=num5+num6
	return resultado

almacena_resultado=suma2(5,25)

print(suma2(2,3))
print(suma2(5,7))
print(suma2(35,358))
print(almacena_resultado)