"""
¿qué hacen? 
Dibuja un punto verde en el centro de la ventana, cada vez que la ventana cambia de tamaño el punto se centra

¿Utilizan éstos funciones (def)? 
Si, utiliza dos

¿Cuáles son las funciones que aparecen? 
setup, screensize, title, hideturtle, penup, goto, dot, pendown, forward, onscreenclick, mainloop

¿Qué hace el programa principal en este caso?
En las funciones onscreenclick llaman a las dos def para centrarlas
"""
from turtle import *

# Crea ventana
setup(450, 200, 0, 0)
screensize(300, 150)
title("www.mclibre.org")
hideturtle()
penup()

def punto(x, y):
    goto(x, y)
    dot(10, "green")

def cuadro(x, y):
    goto(x - 5, y - 5)
    pendown()
    goto(x + 5, y - 5)
    forward(x, y)
    goto(x + 5, y + 5)
    goto(x - 5, y + 5)
    goto(x - 5, y - 5)
    penup()

onscreenclick(punto(5,5))
onscreenclick(cuadro, 3)
mainloop()

