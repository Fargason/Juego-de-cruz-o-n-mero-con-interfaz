from tkinter import *
from random import randint 
import time
import os 
#Especificaciones de la ventana
ventana = Tk()
ventana.title("Juego de cruz o número")
ventana.geometry("400x300")
imagen = PhotoImage(file="Jugar.png")
fondo = Label(ventana,image=imagen).place(x=35,y=30)
lbl_uno = Label(ventana, text="Selección",font=("Arial Bold", 12)).place(x=85,y=4)
lbl_dos = Label(ventana, text="Resultado",font=("Arial Bold", 12)).place(x=225,y=4)
lbl_tres = Label(ventana, text="Usted eligió: ",font=("Arial Bold", 15)).place(x=15,y=190)
#Especificaciones de los botones
ancho_boton=7
alto_boton=2
#Color de los botones y del fondo
ventana.configure(background="ghost white")
color_boton=("gray77")
#Para que los botones sirvan
def btnClick(seleccion):
  global moneda
  moneda=str(seleccion)
  global moneda_2
  moneda_2=str(seleccion)
  input_text.set(moneda)
   #Resultado al azar
  def result_moneda(a: int):
    if a == 0:
     a = str("cruz")
    else:
     a = str("número")
    return a
  #Comparación selección y resultado
  a = randint(0,1)

   # Comparación selección jugador y resultado
  if result_moneda(a) == "cruz" and moneda == "cruz" and tempo(timer)== 0:
    print("\nFelicidades, acerto")
    imagen1 = PhotoImage(file="fotos/cruz.png")
    fondo = Label(ventana,image=imagen1).place(x=50,y=30)
    imagen2 = PhotoImage(file="fotos/result_cruz.png")
    fondo = Label(ventana,image=imagen2).place(x=200,y=30)
    ventana.mainloop()

  elif result_moneda(a) == "número" and moneda == "número" and tempo(timer)== 0:
    print("\nFelicidades, acerto")
    imagen1 = PhotoImage(file="fotos/numero.png")
    fondo = Label(ventana,image=imagen1).place(x=50,y=30)  
    imagen2 = PhotoImage(file="fotos/result_num.png")
    fondo = Label(ventana,image=imagen2).place(x=200,y=30)
    ventana.mainloop()

  elif result_moneda(a) == "cruz" and moneda == "número" and tempo(timer)== 0:
    print("\nMás suerte la proxima vez")
    imagen1 = PhotoImage(file="fotos/numero.png")
    fondo = Label(ventana,image=imagen1).place(x=50,y=30)
    imagen2 = PhotoImage(file="fotos/result_cruz.png")
    fondo = Label(ventana,image=imagen2).place(x=200,y=30)
    ventana.mainloop()

  elif result_moneda(a) == "número" and moneda == "cruz" and tempo(timer)== 0:
    print("\nMás suerte la proxima vez")
    imagen1 = PhotoImage(file="fotos/cruz.png")
    fondo = Label(ventana,image=imagen1).place(x=50,y=30)
    imagen2 = PhotoImage(file="fotos/result_num.png")
    fondo = Label(ventana,image=imagen2).place(x=200,y=30)
    ventana.mainloop() 
    return moneda

#Temporizador
def tempo(timer): 
  print("\nLa moneda esta dando vueltas en el aire...")
  while (timer != 0 ):
    timer=timer-1
    time.sleep(1)
    print ("\nTiempo en el aire...",timer,"s")
    if timer == 0:
      return timer

timer=int(3)

#Boton de limpiar pantalla 
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def reiniciar():
  global moneda
  moneda="Seleccione cruz o número"
  input_text.set(moneda)
  if moneda == "Seleccione cruz o número":
    clearConsole()
    imagen = PhotoImage(file="Jugar.png")
    fondo = Label(ventana,image=imagen).place(x=35,y=30)
    ventana.mainloop()
    return

#Creacion variables para btnClick
input_text=StringVar()
#Creación de los botones
Boton_cruz=Button(ventana,text="cruz",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick("cruz")).place(x=55,y=230)

Boton_numero=Button(ventana,text="número",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClick("número")).place(x=150,y=230)

Boton_reiniciar = Button(ventana, text = "Reiniciar",bg=color_boton,width=ancho_boton,height=alto_boton,command=reiniciar).place(x=245,y=230)

#Creacion de la salida para la selección
Salida = Entry(ventana,font=("arial",10,"bold"),width=23,textvariable=input_text,bd=11,insertwidth=10,bg="powder blue",justify="center").place(x=150,y=182)




