"""t.home() se debe colocar en la linea 24/25 antes de llamar a poligono_regular"""
import turtle as t
lados=7
px=0
py=0
radio=100
angulo = 360 / lados
t.color('green')

for i in range(lados):
    t.penup()
    t.goto(px, py)
    t.pendown()

    t.seth(angulo * i +1) 
    t.forward(radio)

def poligono_regular(px, py, radio, lados):
    t.penup()
    t.goto(px, py - radio)
    t.pendown()
    t.circle(radio)
    t.dot(10, 'green')

t.home()
poligono_regular(px, py, radio, lados)

t.hideturtle()
t.mainloop()
