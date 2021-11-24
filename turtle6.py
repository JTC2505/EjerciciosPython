"""
¿qué hacen? 
Permite dibujar con las teclas del teclado

¿Utilizan éstos funciones (def)? 
Si, utiliza cuatro

¿Cuáles son las funciones que aparecen? 
screen, turtle, forward, setheading, onkeypress, listen, mainloop

¿Qué hace el programa principal en este caso?
espera con la funcion onkeypress que se presiones las teclas del teclado para ejecutar la funcion correspondiente de dibujo
"""
import turtle

#(Nota: Use las teclas de flechas)
window = turtle.Screen()
flecha = turtle.Turtle()

def arriba():
   flecha.setheading(90)
   flecha.forward(100)

def derecha():
   flecha.setheading(0)
   flecha.forward(100)

def abajo():
   flecha.setheading(270)
   flecha.forward(100)

def izquierda():
   flecha.setheading(180)
   flecha.forward(100)


window.onkeypress(arriba, "Up")
window.onkeypress(derecha, "Right")
window.onkeypress(abajo, "Down")
window.onkeypress(izquierda, "Left")

window.listen()
window.mainloop()
