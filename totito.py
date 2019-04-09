#totito
import random
import tkinter
#tkinter libreria  para interfaz gráfica
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog 

color=["#ff7043", "#000000", "#009E6C", "#5e35b1", "#0288d1", "#f44336", "#d4e157"]
    
#ventana del menú
vmenu=Tk()
vmenu.title("Menú totito")
vmenu.geometry("50x50")
#vmenu.geometry("420x270")
vmenu.configure(backg="#2320FC")

#opción salir menú
def salir():
    exit()

#función tablero 1
def tablero1():

#botones juego totito
    for i in range(0,9):
        tablero1.append("X")
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
#variables
menu=Menu(vmenu)
vmenu.config(menu=menu) 
#opciones menú
subm=Menu(menu)
menu.add_cascade(label="Menú Juego Totito", menu=subm)
subm.add_command(label="Juego 1", command=tablero1)
#subm.add_command(label="Juego 2", command=tablero2)
#subm.add_command(label="Juego 3", command=tablero3)
subm.add_command(label="Salir del Juego", command=salir)

#tablero gráfico tkinter
vtablero=Tk()
vtablero.title("------Juego TOTITO 1----")
vtablero.geometry("600x650")
vtablero.configure(backg=random.choice(color))

turno = 0
Jugador1=""
Jugador2=""
listaBotonesm = []
listaBotones = []
tablero1 = [] #variables que se encontraran en el tablero
turnoJugador = StringVar()

#se inicializa tablero
vtablero.mainloop()
vmenu.mainloop()