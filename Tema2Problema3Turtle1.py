import turtle

turtle.setup(350, 350, 0, 0)
turtle.screensize(50, 25)

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