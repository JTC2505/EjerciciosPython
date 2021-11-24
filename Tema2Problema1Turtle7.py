"""
¿qué hacen? 
Dibuja cuadrados hasta formar una especie de circulo sobre puestro sobre otro

¿Utilizan éstos funciones (def)? 
Si, utiliza dos

¿Cuáles son las funciones que aparecen? 
forward, right, speed

¿Qué hace el programa principal en este caso?
Invoca a la funcion espiral, se define la velocidad de dibujo
y se espera que se precione enter para salir
"""
from turtle import *

def cuadrado(longitud):
    # Cuatro veces...
    for i in range(4):
        # Ir hacia adelante
        forward(longitud)
        # Y girar 90 grados
        right(90)

def espiral():
    for i in range(72):
        # Dibujar un cuadrado de 100
        cuadrado(100)
        # Y girar 5 grados
        right(5)


# Yo no quiero animaciones
speed(0)
# Dibujar un espiral
espiral()
# El input es para pausar el programa
input("Presiona Enter para salir...")
