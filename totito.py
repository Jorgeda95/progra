#totito
import random
import tkinter
#tkinter libreria  para interfaz gráfica
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog 

ventana=Tk()
ventana.geometry("600x620")
ventana.title("Juego del totito")
turno = 0
Jugador1=""
Jugador2=""
listaBotones = []
tablero = [] #variables que se encontraran en el tablero
turnoJugador = StringVar()
for i in range(0,9):
    tablero.append("X")
#boton0
boton0=Button(ventana,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton0) 
boton0.place(x=30,y=50)
#boton1
boton1=Button(ventana,width=18,height=8)
listaBotones.append(boton1)
boton1.place(x=230,y=50)
#boton2
boton1=Button(ventana,width=18,height=8)
listaBotones.append(boton1)
boton1.place(x=430,y=50)
#boton3
boton0=Button(ventana,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton0) 
boton0.place(x=30,y=250)
#boton4
boton1=Button(ventana,width=18,height=8)
listaBotones.append(boton1)
boton1.place(x=230,y=250)
#boton5
boton1=Button(ventana,width=18,height=8)
listaBotones.append(boton1)
boton1.place(x=430,y=250)
#boton6
boton0=Button(ventana,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton0) 
boton0.place(x=30,y=450)
#boton7
boton1=Button(ventana,width=18,height=8)
listaBotones.append(boton1)
boton1.place(x=230,y=450)
#boton8
boton1=Button(ventana,width=18,height=8)
listaBotones.append(boton1)
boton1.place(x=430,y=450)




ventana.mainloop()