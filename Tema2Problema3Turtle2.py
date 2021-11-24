import turtle as t
lados=5
px=0
py=0
radio=100
angulo = 360 / lados

for i in range(lados):
   t.forward(160)
   t.right(180 - 36)

def poligono_regular(px, py, radio, lados):
    t.penup()
    t.goto(px + 30, (py - radio) + 5)
    t.pendown()
    for i in range(5):
      t.dot(10, 'black')
      t.forward(radio)
      t.left(72)

t.home()
poligono_regular(px, py, radio, lados)

t.hideturtle()
t.mainloop()