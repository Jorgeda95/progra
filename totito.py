#totito
import random
import tkinter
#tkinter libreria  para interfaz gráfica
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog 

color=["#ff7043", "#000000", "#009E6C", "#5e35b1", "#0288d1", "#f44336", "#d4e157"]
comenzarc=("#ff80ab")
textobtn=("#FFFFFF")
negro=("#000000")
#clase Tk convertida en tkinter
tkin=Tk
tventana=("600x750")
turno = 0
Jugador1=""
Jugador2=""
Computadora=["Corn", "Tosk", "Rabito", "Spiki", "Triki", "Ham-jam", "Jujo", "Sirgo", "Vomi-t", "Weypo", "Lopini", "Juralio", "Cerki", "Laleña", "Ñopir", "Canfi", "Ufito", "Sansal","Aporito","Boliza","Batiman","Iron-oxidado"] 
listaBotones = []
t1 = [] #variables que se encontraran en el tablero # X O N
t2 = []
t3 = []
#ventana del menú
vmenu=tkin()
vmenu.title("Menú totito")
vmenu.geometry("710x60")
#vmenu.geometry("420x270")
vmenu.configure(backg="#2320FC")
ins = Label(vmenu,bg=comenzarc, fg=textobtn,font=("Roboto",15), text="Instrucciones: Primer paso:Escoja un tablero \n Segundo paso: Escoja el número de Juego (ambos deben ser el mismo número)").pack()

def blok():
    for i in range(0,9):
        listaBotones[i].config(state="disable")

#Se comienza y desbloquea el juego
def comenzarJuego():
    
    for i in range(0,9):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(text="")#se limpian los botones
        t1[i] = "N"
    
    global Jugador1, Jugador2
    Jugador1 = simpledialog.askstring("Jugador #1", "Ingrese el nombre del Jugador #1: ")
    Jugador2 = simpledialog.askstring("Jugador #2", "Ingrese el nombre del Jugador #2: ")
    turnoJugador = StringVar()
    turnoJugador.set(Jugador1)
    label = Label(vtablero, text="Nombre")
    label.pack(anchor="center")
    label.config(bg=comenzarc, fg=textobtn, font=("Roboto",20))
    label.config(textvariable=turnoJugador)

def comenzarJuego2():
    
    for i in range(0,9):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(text="")#se limpian los botones
        t2[i] = "N"
    
    global Jugador1, Computadora
    Jugador1 = simpledialog.askstring("Jugador #1", "Ingrese el nombre del Jugador #1: ")
    Compu=str(random.choice(Computadora))
    turnoJugador = StringVar()
    turnoJugador.set(Jugador1)
    label = Label(vtablero, text="Nombre")
    label.pack(anchor="center")
    label.config(bg=comenzarc, fg=textobtn, font=("Roboto",20))
    label.config(textvariable=turnoJugador)

def comenzarJuego3():
    
    for i in range(0,9):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(text="")#se limpian los botones
        t3[i] = "N"
    
    global Jugador1, Jugador2
    Jugador1 = (input("Ingrese el nombre del Jugador #1: "))
    Jugador2 = (input("Ingrese el nombre del Jugador #2: "))
    Jugadores=["Jugador1", "Jugador2"]
    turnoJugador = StringVar()
    turnoJugador.set(Jugadores)
    label = Label(vtablero, textvariable=random.choice(Jugadores))
    label.pack(anchor="center")
    label.config(bg=comenzarc, fg=textobtn, font=("Roboto",20))
    label.config(textvariable=turnoJugador)

def cambiar(num):
    global turno,Jugador1,Jugador2
    if t1[num]=="N" and turno == 0:
        listaBotones[num].config(text="X")
        listaBotones[num].config(bg=textobtn)
        t1[num]="X"
        turno = 1
        turnoJugador.set("Turno de:" + "Jugador2")

    elif t1[num]=="N" and turno ==1:
        listaBotones[num].config(text="O")
        listaBotones[num].config(bg="#cfd8dc")
        t1[num]="O"
        turno = 0
        turnoJugador.set("Turno de:" + "Jugador1")
    listaBotones[num].config(state="disable")

def cambiar3(num):
    global turno,Jugador1,Jugador2
    if t3[num]=="N" and turno == 0:
        listaBotones[num].config(text="X")
        listaBotones[num].config(bg=textobtn)
        t3[num]="X"
        turno = 1
        turnoJugador.set("Turno de:" + "Jugador2")

    elif t3[num]=="N" and turno ==1:
        listaBotones[num].config(text="O")
        listaBotones[num].config(bg="#cfd8dc")
        t3[num]="O"
        turno = 0
        turnoJugador.set("Turno de:" + "Jugador1")
    listaBotones[num].config(state="disable")

def ganador():
    #gano Xhorizontal
    if (t1[0]=="X" and t1[1]=="X" and t1[2]=="X") or (t1[3]=="X" and t1[4]=="X" and t1[5]=="X") or (t1[6]=="X" and t1[7]=="X" and t1[8]=="X"):
        blok()
        messagebox.showinfo("Gano", "Perdiste Jugador"+ "Jugador1")
    #gano X vertical
    elif (t1[0]=="X" and t1[3]=="X" and t1[6]=="X") or (t1[1]=="X" and t1[4]=="X" and t1[7]=="X") or (t1[2]=="X" and t1[5]=="X" and t1[8]=="X"):
        blok()
        messagebox.showinfo("Gano", "Perdiste Jugador"+ "Jugador1")
    #gana X cruzado
    elif (t1[0]=="X" and t1[4]=="X" and t1[8]=="X") or (t1[2]=="X" and t1[4]=="X" and t1[6]=="X"):
        blok()
        messagebox.showinfo("Gano", "Perdiste Jugador"+ "Jugador1")
    #gano O horizontal
    elif (t1[0]=="O" and t1[1]=="O" and t1[2]=="O") or (t1[3]=="O" and t1[4]=="O" and t1[5]=="O") or (t1[6]=="O" and t1[7]=="O" and t1[8]=="O"):
        blok()
    messagebox.showinfo("Gano", "Perdiste Jugador"+ "Jugador2")
    #gano O vertical
    if (t1[0]=="O" and t1[3]=="O" and t1[6]=="O") or (t1[1]=="O" and t1[4]=="O" and t1[7]=="O") or (t1[2]=="O" and t1[5]=="O" and t1[8]=="O"):
        blok()
        messagebox.showinfo("Gano", "Perdiste Jugador"+ "Jugador2")
    #gana O cruzado
    elif (t1[0]=="O" and t1[4]=="O" and t1[8]=="O") or (t1[2]=="O" and t1[4]=="O" and t1[6]=="O"):
        blok()
        messagebox.showinfo("Gano", "Perdiste Jugador"+ "Jugador2")

#verifica el ganador de misere
def ganador3():
    #Perdio Xhorizontal
    if (t3[0]=="X" and t3[1]=="X" and t3[2]=="X") or (t3[3]=="X" and t3[4]=="X" and t3[5]=="X") or (t3[6]=="X" and t3[7]=="X" and t3[8]=="X"):
        blok()
        messagebox.showinfo("Perdio", "Perdiste Jugador"+ "Jugador1")
    #Perdio X vertical
    elif (t3[0]=="X" and t3[3]=="X" and t3[6]=="X") or (t3[1]=="X" and t3[4]=="X" and t3[7]=="X") or (t3[2]=="X" and t3[5]=="X" and t3[8]=="X"):
        blok()
        messagebox.showinfo("Perdio", "Perdiste Jugador"+ "Jugador1")
    #Perdio X cruzado
    elif (t3[0]=="X" and t3[4]=="X" and t3[8]=="X") or (t3[2]=="X" and t3[4]=="X" and t3[6]=="X"):
        blok()
        messagebox.showinfo("Perdio", "Perdiste Jugador"+ "Jugador1")
    #Perdio O horizontal
    elif (t3[0]=="O" and t3[1]=="O" and t3[2]=="O") or (t3[3]=="O" and t3[4]=="O" and t3[5]=="O") or (t3[6]=="O" and t3[7]=="O" and t3[8]=="O"):
        blok()
    messagebox.showinfo("Perdio", "Perdiste Jugador"+ "Jugador2")
    #Perdio O vertical
    if (t3[0]=="O" and t3[3]=="O" and t3[6]=="O") or (t3[1]=="O" and t3[4]=="O" and t3[7]=="O") or (t3[2]=="O" and t3[5]=="O" and t3[8]=="O"):
        blok()
        messagebox.showinfo("Perdio", "Perdiste Jugador"+ "Jugador2")
    #Perdio O cruzado
    elif (t3[0]=="O" and t3[4]=="O" and t3[8]=="O") or (t3[2]=="O" and t3[4]=="O" and t3[6]=="O"):
        blok()
        messagebox.showinfo("Perdio", "Perdiste Jugador"+ "Jugador2")

#Main menu para deshabilitar y habilitar las otras ventas
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
    

#opción salir menú
def salir():
        exit()

#función tablero 1
def tablero1():
#botones juego totito

    for i in range(0,9):
        t1.append("N")
    #boton0
    boton0=Button(vtablero,width=18,height=8,command=lambda: cambiar(0))
    listaBotones.append(boton0) 
    boton0.place(x=30,y=50)
    #boton1
    boton1=Button(vtablero,width=18,height=8,command=lambda: cambiar(1))
    listaBotones.append(boton1)
    boton1.place(x=230,y=50)
    #boton2
    boton2=Button(vtablero,width=18,height=8,command=lambda: cambiar(2))
    listaBotones.append(boton2)
    boton2.place(x=430,y=50)
    #boton3
    boton3=Button(vtablero,width=18,height=8,command=lambda: cambiar(3))
    listaBotones.append(boton3) 
    boton3.place(x=30,y=250)
    #boton4
    boton4=Button(vtablero,width=18,height=8,command=lambda: cambiar(4))
    listaBotones.append(boton4)
    boton4.place(x=230,y=250)
    #boton5
    boton5=Button(vtablero,width=18,height=8,command=lambda: cambiar(5))
    listaBotones.append(boton5)
    boton5.place(x=430,y=250)
    #boton6
    boton6=Button(vtablero,width=18,height=8,command=lambda: cambiar(6))
    listaBotones.append(boton6) 
    boton6.place(x=30,y=450)
    #boton7
    boton7=Button(vtablero,width=18,height=8,command=lambda: cambiar(7))
    listaBotones.append(boton7)
    boton7.place(x=230,y=450)
    #boton8
    boton8=Button(vtablero,width=18,height=8,command=lambda: cambiar(8))
    listaBotones.append(boton8)
    boton8.place(x=430,y=450)

    comenzar = Button(vtablero,bg=comenzarc, fg=textobtn,font=("Roboto",14),text="Jugar!!!", width=15,height=3, command=comenzarJuego).place(x=80, y=610)
    salirj = Button(vtablero,bg=comenzarc, fg=textobtn,font=("Roboto",14),text="--Salir--", width=15,height=3, command=salir).place(x=320, y=610)
    blok()

#función tablero 2
def tablero2():
#botones juego totito
    for i in range(0,9):
        t2.append("N")
    #boton0
    boton0=Button(vtablero2,width=20,height=8,command=lambda: cambiar(0))
    listaBotones.append(boton0) 
    boton0.place(x=30,y=50)
    #boton1
    boton1=Button(vtablero2,width=20,height=8,command=lambda: cambiar(1))
    listaBotones.append(boton1)
    boton1.place(x=230,y=50)
    #boton2
    boton2=Button(vtablero2,width=20,height=8,command=lambda: cambiar(2))
    listaBotones.append(boton2)
    boton2.place(x=430,y=50)
    #boton3
    boton3=Button(vtablero2,width=20,height=8,command=lambda: cambiar(3))
    listaBotones.append(boton3) 
    boton3.place(x=30,y=250)
    #boton4
    boton4=Button(vtablero2,width=20,height=8,command=lambda: cambiar(4))
    listaBotones.append(boton4)
    boton4.place(x=230,y=250)
    #boton5
    boton5=Button(vtablero2,width=20,height=8,command=lambda: cambiar(5))
    listaBotones.append(boton5)
    boton5.place(x=430,y=250)
    #boton6
    boton6=Button(vtablero2,width=20,height=8,command=lambda: cambiar(6))
    listaBotones.append(boton6) 
    boton6.place(x=30,y=450)
    #boton7
    boton7=Button(vtablero2,width=20,height=8,command=lambda: cambiar(7))
    listaBotones.append(boton7)
    boton7.place(x=230,y=450)
    #boton8
    boton8=Button(vtablero2,width=20,height=8,command=lambda: cambiar(8))
    listaBotones.append(boton8)
    boton8.place(x=430,y=450)

    comenzar2 = Button(vtablero2,bg=comenzarc, fg=textobtn,font=("Roboto",14),text="Jugar!!!", width=15,height=3, command=comenzarJuego2).place(x=80, y=610)
    salirj = Button(vtablero2,bg=comenzarc, fg=textobtn,font=("Roboto",14),text="--Salir--", width=15,height=3, command=salir).place(x=320, y=610)
    blok()

def tablero3():
#botones juego totito
    for i in range(0,9):
        t3.append("N")
    #boton0
    boton0=Button(vtablero3,width=20,height=8,command=lambda: cambiar3(0))
    listaBotones.append(boton0) 
    boton0.place(x=30,y=50)
    #boton1
    boton1=Button(vtablero3,width=20,height=8,command=lambda: cambiar3(1))
    listaBotones.append(boton1)
    boton1.place(x=230,y=50)
    #boton2
    boton2=Button(vtablero3,width=20,height=8,command=lambda: cambiar3(2))
    listaBotones.append(boton2)
    boton2.place(x=430,y=50)
    #boton3
    boton3=Button(vtablero3,width=20,height=8,command=lambda: cambiar3(3))
    listaBotones.append(boton3) 
    boton3.place(x=30,y=250)
    #boton4
    boton4=Button(vtablero3,width=20,height=8,command=lambda: cambiar3(4))
    listaBotones.append(boton4)
    boton4.place(x=230,y=250)
    #boton5
    boton5=Button(vtablero3,width=20,height=8,command=lambda: cambiar3(5))
    listaBotones.append(boton5)
    boton5.place(x=430,y=250)
    #boton6
    boton6=Button(vtablero3,width=20,height=8,command=lambda: cambiar3(6))
    listaBotones.append(boton6) 
    boton6.place(x=30,y=450)
    #boton7
    boton7=Button(vtablero3,width=20,height=8,command=lambda: cambiar3(7))
    listaBotones.append(boton7)
    boton7.place(x=230,y=450)
    #boton8
    boton8=Button(vtablero3,width=20,height=8,command=lambda: cambiar3(8))
    listaBotones.append(boton8)
    boton8.place(x=430,y=450)

    comenzar3 = Button(vtablero3,bg=comenzarc, fg=textobtn,font=("Roboto",14),text="Jugar!!!", width=15,height=3, command=comenzarJuego3).place(x=80, y=610)
    salirj = Button(vtablero3,bg=comenzarc, fg=textobtn,font=("Roboto",14),text="--Salir--", width=15,height=3, command=salir).place(x=320, y=610)
    blok()

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
vtablero.title("------Juego TOTITO Normal----")
vtablero.geometry(tventana)
vtablero.configure(backg=random.choice(color))
mtablero = Label(vtablero,fg=negro,font=("Roboto",7), text=""" 
012    _|_|_
 345    _|_|_
  678    _|_|_""").place(x=50,y=1)


vtablero2=tkin()
vtablero2.withdraw()
vtablero2.title("------Juego TOTITO 2 vs Computadora----")
vtablero2.geometry(tventana)
vtablero2.configure(backg=random.choice(color))
mtablero = Label(vtablero2,fg=negro,font=("Roboto",7), text=""" 
012    _|_|_
 345    _|_|_
  678    _|_|_""").place(x=50,y=1)

vtablero3=tkin()
vtablero3.withdraw()
vtablero3.title("------Juego TOTITO 3 Misere----")
vtablero3.geometry(tventana)
vtablero3.configure(backg=random.choice(color))
mtablero = Label(vtablero3,fg=negro,font=("Roboto",7), text=""" 
012    _|_|_
 345    _|_|_
  678    _|_|_""").place(x=50,y=1)

turnoJugador = StringVar()

'''
#Venta de texto prueba
prueba = tkin()
Jugador1=simpledialog.askstring("Jugador #1","Ingrese el nombre del Jugador #1: ")
turnoJugador = StringVar()
turnoJugador.set(Jugador1)
label = Label(prueba, text="Esto es una prueba")
label.pack(anchor="center")
label.config(bg="green", fg="blue", font=("Robot",20))
label.config(textvariable=turnoJugador)
prueba.mainloop()
'''

#se inicializa tablero
vtablero.mainloop()
vtablero2.mainloop()
vtablero3.mainloop()
vmenu.mainloop()