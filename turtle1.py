"""
¿qué hacen? 
Permite dibujar punto dando click en la pantalla

¿Utilizan éstos funciones (def)? 
Si, utiliza una

¿Cuáles son las funciones que aparecen? 
setup, screensize, title, hideturtle, penup, onscreenclick, mainloop

¿Qué hace el programa principal en este caso?
Redimenciona la ventana, oculta la tortuga y nombra la ventana
"""
from turtle import *

setup(450, 200, 0, 0)
screensize(300, 150)
title("www.mclibre.org")
hideturtle()
penup()

def punto(x, y):
    goto(x, y)
    dot(10, "black")

onscreenclick(punto)
mainloop()
