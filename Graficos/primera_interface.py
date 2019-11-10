from tkinter import *

#----Creamos la raiz------
raiz =Tk()
raiz.title("Ventana de prueba")
raiz.resizable(1,1) #Nos permite redimensionar la ventana: 0-false / 1-true
raiz.iconbitmap("02.ico") #Nos permite poner una imagen en lugar de la pluma. Tiene que tener formato *.ico
	#Si lo ponemos en el mismo directorio donde está *py, o hace falta poner la dirección completa
raiz.geometry("480x350") #ancho x alto
raiz.config(bg="light blue")


#----Creamos el frame
miFrame=Frame() #Con esto contruimos el frame y lo metemos dentro de la raiz
#Este frame debemos empaquetarlo, es decir, meterlo dentro de la raiz
miFrame.pack()
miFrame.config(bg="red")
#Para darle tamaño a un frame, hay que quitarle el tamaño a la raiz (raiz.geometry("480x350"))
#   En este caso, la raiz se adpata al tamaño del frame. Si no quitasemos el tamaño de la raiz,
#    la raiz se vería
miFrame.config(width="400", height="300")
#Ajustamos el frame a la derecha y arriba (n, s,w,e)
# miFrame.pack(side="right")#, anchor="n")

#Estos dos métodos debe utilizarse conjuntamente
#Expande el frame a lo largo del eje y
# miFrame.pack(fill="both")
#Permite que el frame se expanda al modificar el tamaño de la raiz
# miFrame.pack(expand=0)


#Cambiamos el tipo de borde y el grosor
miFrame.config(bd=10)
miFrame.config(relief="raised") #"raised", "sunken", "flat", "groove", and "ridge".

#Cambiamos el tipo de puntero del ratón al pasar por el frame.
miFrame.config(cursor="pirate")



#El método mainloop debe estar en último lugar
raiz.mainloop()
#Con estas tres primeras instrucciones hemos creado nuestra ventana
# from tkinter import *
# raiz =Tk()
# raiz.mainloop()

#Documentacion sobre tkinter= https://docs.python.org/3.8/library/tkinter.html

# Si la extensión la cambiamos de *.py a *.pyw, al hacer doble clic, 
#    nos aparecerá la ventana sin la consola de python.
