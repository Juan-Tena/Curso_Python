from  tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

#Texto
miLabel=Label(miFrame, text="Hola alumnos de python",fg="blue", font=("Verdana",18))
miLabel.place(x=100, y=200) #Nos permite ubicar el texto el cualquier parte del frame
#Imagen
miImagen=PhotoImage(file="02.gif")
Label(miFrame, image=miImagen).place(x=150, y=250)
#Texto)
miLabel1=Label(miFrame, text="Hola alumnos de Python",fg="blue", font=("Verdana",18))
miLabel1.place(x=50, y=300) #Nos permite ubicar el texto el cualquier parte del frame

root.mainloop()