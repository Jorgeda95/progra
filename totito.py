#totito
import random
import tkinter
#tkinter libreria  para interfaz gráfica
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog 


#acciones menu

    
#ventana del menú
vmenu=Tk()
vmenu.title("Menú totito")
vmenu.geometry("420x270")
vmenu.configure(backg="#2320FC")

menu=Menu(vmenu)
vmenu.config(menu=menu) 

def salir():
    exit()

subm=Menu(menu)
menu.add_cascade(label="Menú Juego Totito", menu=subm)
subm.add_command(label="Juego 1")
subm.add_command(label="Juego 2")
subm.add_command(label="Juego 3")
subm.add_command(label="Salir del Juego", command=salir)



#tablero del juego
vtablero=Tk()
vtablero.title("------Juego TOTITO----")
vtablero.geometry("600x650")
vtablero.configure(backg="#009E6C")

turno = 0
Jugador1=""
Jugador2=""
listaBotonesm = []
listaBotones = []
tablero = [] #variables que se encontraran en el tablero
turnoJugador = StringVar()

#btn menú totito
for i in range(0,4):
    tablero.append("X")
#boton menu 0 (modo 1)
btnm0=Button(vmenu,width=15,height=5)#command=cambiar(0)
listaBotonesm.append(btnm0) 
btnm0.place(x=30,y=50)
#boton menu 1 (modo 2)
btnm0=Button(vmenu,width=15,height=5)#command=cambiar(0)
listaBotonesm.append(btnm0) 
btnm0.place(x=150,y=50)
#boton menu 2 (modo 3)
btnm0=Button(vmenu,width=15,height=5)#command=cambiar(0)
listaBotonesm.append(btnm0) 
btnm0.place(x=270,y=50)
#boton menu 3 (salida)
btnm0=Button(vmenu,width=20,height=3)#command=cambiar(0)
listaBotonesm.append(btnm0) 
btnm0.place(x=130,y=170)



# def tablero():


#btn juego totito
for i in range(0,9):
    tablero.append("X")
#boton0
boton0=Button(vtablero,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton0) 
boton0.place(x=30,y=50)
#boton1
boton1=Button(vtablero,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton1)
boton1.place(x=230,y=50)
#boton2
boton2=Button(vtablero,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton2)
boton2.place(x=430,y=50)
#boton3
boton3=Button(vtablero,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton3) 
boton3.place(x=30,y=250)
#boton4
boton4=Button(vtablero,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton4)
boton4.place(x=230,y=250)
#boton5
boton5=Button(vtablero,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton5)
boton5.place(x=430,y=250)
#boton6
boton6=Button(vtablero,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton6) 
boton6.place(x=30,y=450)
#boton7
boton7=Button(vtablero,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton7)
boton7.place(x=230,y=450)
#boton8
boton8=Button(vtablero,width=18,height=8)#command=cambiar(0)
listaBotones.append(boton8)
boton8.place(x=430,y=450)



vtablero.mainloop()
vmenu.mainloop()