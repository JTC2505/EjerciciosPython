"""
¿qué hacen? 
dibuja 3 figuras, un triangulo, un cuadrado y un pentagono una sobre otra

¿Utilizan éstos funciones (def)? 
Si, utiliza tres

¿Cuáles son las funciones que aparecen? 
screen, turtle, forward, left

¿Qué hace el programa principal en este caso?
invovoca las funciones que dibujan el triangulo, cuadrado y pentagono en ese respectivo orden
"""
import turtle

window = turtle.Screen()
flecha = turtle.Turtle()

def triangulo():
   for i in range(3):
      flecha.forward(100)
      flecha.left(120)

def cuadrado():
   for i in range(4):
      flecha.forward(100)
      flecha.left(90)

def pentagono():
   for i in range(5):
      flecha.forward(100)
      flecha.left(72)

triangulo()
cuadrado()
pentagono()
