from Tema1Problema2Modulo import *

continuar = 's'
while continuar == 's' or continuar == 'S':
    print('\nVentas realizadas(cantidades): ')
    desayunos = float(input('Total desayunos: '))
    almuerzos = float(input('Total almuerzos: '))
    cenas = float(input('Total cenas: '))

    print('\nPrecios tiempos: ')
    desayunosSub = float(input('Por favor ingrese el valor del desayuno: '))
    almuerzosSub = float(input('Por favor ingrese el valor del almuerzo: '))
    cenasSub = float(input('Por favor ingrese el valor de la cena: '))

    print('Estos son los resultados: ')
    print(f'Total desayunos: {totalTiempo(desayunos, desayunosSub)}')
    print(f'Total almuerzos: {totalTiempo(almuerzos, almuerzosSub)}')
    print(f'Total cenas: {totalTiempo(cenas, cenasSub)}')
    print(f'TOTAL: {sumaTotal(totalTiempo(desayunos, desayunosSub), totalTiempo(almuerzos, almuerzosSub), totalTiempo(cenas, cenasSub))}')

    print('\ndesea hacer este proceso otra vez? (s/n)')
    continuar = input()