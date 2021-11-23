def Potencia(x, n):
    resultado = 1
    for i in range(1, n):
        resultado = resultado * x
    return resultado

def Factorial(x):
    resultado = 1
    for i in range(1, x + 1):
        resultado = resultado * i
    return resultado

def DivEntera(x, n):
    if x % n == 0:
        print('La division es entera')
    elif n == 0:
        print('La division no se puede realizar entre cero')
    else:
        print('La division no es entera')