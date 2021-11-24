"""
¿qué hacen? 
Dibuja una estrella

¿Utilizan éstos funciones (def)? 
Si, utiliza una

¿Cuáles son las funciones que aparecen? 
forward, right, speed

¿Qué hace el programa principal en este caso?
llama a la funcion speed para establecer la velocidad de pintado de la estrella
tambien llama a la funcion estrella que es la que la dibuja
y espera a que se presione enter para finalizar el programa
"""
from turtle import *

def estrella(longitud):
    for i in range(5):
        forward(longitud)
        right(180 - 36)

# Yo no quiero animaciones
speed(5)
# Dibujar estrella de 100
estrella(100)
# El input es para pausar el programa
input("Presiona Enter para salir...")
