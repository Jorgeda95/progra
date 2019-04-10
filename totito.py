#totito
import random
import tkinter
#tkinter libreria  para interfaz gráfica
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog 

color=["#ff7043", "#000000", "#009E6C", "#5e35b1", "#0288d1", "#f44336", "#d4e157"]
#clase Tk convertida en tkinter
tkin=Tk
tventana=("600x650")

#ventana del menú
vmenu=tkin()
vmenu.title("Menú totito")
vmenu.geometry("50x50")
#vmenu.geometry("420x270")
vmenu.configure(backg="#2320FC")

#Main menu

def otraventana():
    vtablero.state(newstate='normal')
    vtablero2.state(newstate='withdraw')
    vtablero3.state(newstate='withdraw')    
def otraventana2():
    vtablero2.state(newstate='normal')
    vtablero.state(newstate='withdraw')
    vtablero3.state(newstate='withdraw')
    
def otraventana3():
    vtablero3.state(newstate='normal')
    vtablero2.state(newstate='withdraw')
    vtablero.state(newstate='withdraw')
    
    
    '''
    otra_ventana = tkinter.Toplevel(vmenu)
    vtablero.wm_deiconify()

def otraventana1():
    otra_ventana1 = tkinter.Toplevel(vmenu)
    vtablero2.wm_deiconify()
def otraventana2():
    otra_ventana2 = tkinter.Toplevel(vmenu)
    vtablero3.wm_deiconify()
'''
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
#función tablero 2
def tablero2():
#botones juego totito
    for i in range(0,9):
        tablero2.append("X")
    #boton0
    boton0=Button(vtablero2,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton0) 
    boton0.place(x=30,y=50)
    #boton1
    boton1=Button(vtablero2,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton1)
    boton1.place(x=230,y=50)
    #boton2
    boton2=Button(vtablero2,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton2)
    boton2.place(x=430,y=50)
    #boton3
    boton3=Button(vtablero2,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton3) 
    boton3.place(x=30,y=250)
    #boton4
    boton4=Button(vtablero2,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton4)
    boton4.place(x=230,y=250)
    #boton5
    boton5=Button(vtablero2,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton5)
    boton5.place(x=430,y=250)
    #boton6
    boton6=Button(vtablero2,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton6) 
    boton6.place(x=30,y=450)
    #boton7
    boton7=Button(vtablero2,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton7)
    boton7.place(x=230,y=450)
    #boton8
    boton8=Button(vtablero2,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton8)
    boton8.place(x=430,y=450)


def tablero3():
#botones juego totito
    for i in range(0,9):
        tablero2.append("X")
    #boton0
    boton0=Button(vtablero3,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton0) 
    boton0.place(x=30,y=50)
    #boton1
    boton1=Button(vtablero3,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton1)
    boton1.place(x=230,y=50)
    #boton2
    boton2=Button(vtablero3,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton2)
    boton2.place(x=430,y=50)
    #boton3
    boton3=Button(vtablero3,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton3) 
    boton3.place(x=30,y=250)
    #boton4
    boton4=Button(vtablero3,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton4)
    boton4.place(x=230,y=250)
    #boton5
    boton5=Button(vtablero3,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton5)
    boton5.place(x=430,y=250)
    #boton6
    boton6=Button(vtablero3,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton6) 
    boton6.place(x=30,y=450)
    #boton7
    boton7=Button(vtablero3,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton7)
    boton7.place(x=230,y=450)
    #boton8
    boton8=Button(vtablero3,width=20,height=8)#command=cambiar(0)
    listaBotones.append(boton8)
    boton8.place(x=430,y=450)

#variables
menu=Menu(vmenu)
vmenu.config(menu=menu) 

#opciones menú
subm=Menu(menu)
menu.add_cascade(label="Menú Juego Totito", menu=subm)
subm.add_command(label="Tablero 1",command=otraventana)
subm.add_command(label="Tablero 2",command=otraventana2)
subm.add_command(label="Tablero 3",command=otraventana3)
subm.add_command(label="Juego 1", command=tablero1)
subm.add_command(label="Juego 2", command=tablero2) 
subm.add_command(label="Juego 3", command=tablero3)
subm.add_command(label="Salir del Juego", command=salir)

#tablero gráfico tkinter
vtablero=tkin()
vtablero.withdraw()
vtablero.title("------Juego TOTITO----")
vtablero.geometry(tventana)
vtablero.configure(backg=random.choice(color))

vtablero2=tkin()
vtablero2.withdraw()
vtablero2.title("------Juego TOTITO 2----")
vtablero2.geometry(tventana)
vtablero2.configure(backg=random.choice(color))

vtablero3=tkin()
vtablero3.withdraw()
vtablero3.title("------Juego TOTITO 3----")
vtablero3.geometry(tventana)
vtablero3.configure(backg=random.choice(color))

turno = 0
Jugador1=""
Jugador2=""
listaBotonesm = []
listaBotones = []
tablero1 = [] #variables que se encontraran en el tablero
tablero2 = []
turnoJugador = StringVar()

#se inicializa tablero
vtablero.mainloop()
vtablero2.mainloop()
vtablero3.mainloop()
vmenu.mainloop()