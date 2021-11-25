from Tema1Problema1Modulo import *

continuar = 's'
while continuar == 's' or continuar == 'S':
    km = float(input('Por favor ingrese los km a convertir: '))
    eur = float(input('Por favor ingrese los eur a convertir: '))
    l = float(input('Por favor ingrese los l a convertir: '))

    print('Estos son los resultados: ')
    print(f'km a mi: {kmAMi(km)}')
    print(f'eur a usd: {EurAUSD(eur)}')
    print(f'l a gal: {lAGal(l)}')

    print('\ndesea hacer este proceso otra vez? (s/n)')
    continuar = input()