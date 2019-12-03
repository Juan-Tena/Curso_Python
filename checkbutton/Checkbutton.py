from tkinter import *

root=Tk()
root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViaje():
	opcionEscogina=""

	if(playa.get()==1):
		opcionEscogina+=" playa"
	if(montagna.get()==1):
		opcionEscogina+=" montaña"
	if(turismoRural.get()==1):
		opcionEscogina+=" turismo rural"

	textoFinal.config(text=opcionEscogina)

foto=PhotoImage(file="02.gif")
Label(root,image=foto).pack()

frame=Frame(root).pack()
#frame.pack()

Label(frame, text="Elige destino", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña",variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo Rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()