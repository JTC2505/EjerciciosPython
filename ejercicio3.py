from ejercicio3Modulo import *

opcion = 1
while opcion != 4:
    print('\n1.- Potencia de un numero')
    print('2.- Factorial de un numero')
    print('3.- Division entera')
    print('4.- Salir')
    opcion = int(input())
    if opcion == 1:
        x = int(input('Ingrese el valor de x: '))
        n = int(input('Ingrese el valor de n: '))
        print(f'Total potencia de {x} a la {n} veces: {Potencia(x, n)}')
    elif opcion == 2:
        x = int(input('Ingrese el valor de x: '))
        print(f'Factorial de {x}: {Factorial(x)}')
    elif opcion == 3:
        x = int(input('Ingrese el valor de x: '))
        n = int(input('Ingrese el valor de n: '))
        DivEntera(x, n)
    elif opcion == 4:
        print('Saliendo...')
    else:
        print('Opcion ingresada invalida')
