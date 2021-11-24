"""
¿qué hacen? 
Dibuja 3 figuras, un triangulo, un cuadrado y un pentagono una sobre otra

¿Utilizan éstos funciones (def)? 
Si, utiliza una

¿Cuáles son las funciones que aparecen? 
screen, turtle, forward, left

¿Qué hace el programa principal en este caso?
Envia a la funcion figura el numero de lados y en base a ello dibuja la figura correspondiente
"""
import turtle

window = turtle.Screen()
flecha = turtle.Turtle()

def figura(lados):
   for i in range(lados):
      flecha.forward(100)
      flecha.left(360/lados)

figura(3)
figura(4)
figura(5)