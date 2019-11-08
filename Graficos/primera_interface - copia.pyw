from tkinter import *

raiz =Tk()
raiz.title("Ventana de prueba")
raiz.resizable(0,0) #Nos permite redimensionar la ventana: 0-false / 1-true
raiz.iconbitmap("02.ico") #Nos permite poner una imagen en lugar de la pluma. Tiene que tener formato *.ico
	#Si lo ponemos en el mismo directorio donde está *py, o hace falta poner la dirección completa
raiz.geometry("480x350") #ancho x alto
raiz.config(bg="light blue")


#El método mainloop debe estar en último lugar
raiz.mainloop()
#Con estas tres primeras instrucciones hemos creado nuestra ventana
# from tkinter import *
# raiz =Tk()
# raiz.mainloop()

#Documentacion sobre tkinter= https://docs.python.org/3.8/library/tkinter.html

