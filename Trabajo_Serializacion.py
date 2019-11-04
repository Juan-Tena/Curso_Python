import pickle

lista_nombres=["Pedro", "Ana", "Maria","Isabel"]

fichero_binario=open("lista_nombre","wb") #Escritura binaria

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario)

#Ahora, una vez creado el fichero binario, vamos a rescatar la información que contiene
import pickle
fichero=open("lista_nombre", "rb")
lista=pickle.load(fichero)
print(lista)