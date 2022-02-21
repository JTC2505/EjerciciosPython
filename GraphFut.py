# Hacer un programa que lea en un arreglo los resultados por fecha (1=gano, 0=perdió) de los equipos que participan en un campeonato. 
# Luego, el programa deberá calcular la gráfica de partidos ganados y partidos perdidos.
from GraphFutModulo import *
import itertools
import matplotlib.pyplot as plt
import numpy as np

resultado = ''
partidosE1 = []
partidosE2 = []
partidosE3 = []
partidosE4 = []
contador0 = 0
contador1 = 0
nombres = ['','','','']
print('Bienvenido/a al sistema de graficas sobre partidos de 4 equipos')
nombres[0] = input('\nIngrese el nombre del equipo 1: ')
nombres[1] = input('\nIngrese el nombre del equipo 2: ')
nombres[2] = input('\nIngrese el nombre del equipo 3: ')
nombres[3] = input('\nIngrese el nombre del equipo 4: ')
e = itertools.combinations(nombres, 2)
for i in e:
    print('\nQuien gano el partido en el encuentro ' + i[0] + ' vs ' + i[1] + '?')
    print('\n 1.- ' + i[0])
    print('\n 2.- ' + i[1])
    resultado = input('')
    if(resultado == '1'):
        equipoG(Noequipo(i[0], nombres), partidosE1, partidosE2, partidosE3, partidosE4)
        equipoP(Noequipo(i[1], nombres), partidosE1, partidosE2, partidosE3, partidosE4)
    else:
        equipoG(Noequipo(i[1], nombres), partidosE1, partidosE2, partidosE3, partidosE4)
        equipoP(Noequipo(i[0], nombres), partidosE1, partidosE2, partidosE3, partidosE4)

resultados = {
    'ganados':[],
    'perdidos':[]
}
for x in partidosE1:
    if(x == 1):
        contador1 += 1
    else:
        contador0 += 1
resultados['ganados'].append(contador1)
resultados['perdidos'].append(contador0)
contador0 = 0
contador1 = 0
for x in partidosE2:
    if(x == 1):
        contador1 += 1
    else:
        contador0 += 1
resultados['ganados'].append(contador1)
resultados['perdidos'].append(contador0)
contador0 = 0
contador1 = 0
for x in partidosE3:
    if(x == 1):
        contador1 += 1
    else:
        contador0 += 1
resultados['ganados'].append(contador1)
resultados['perdidos'].append(contador0)
contador0 = 0
contador1 = 0
for x in partidosE4:
    if(x == 1):
        contador1 += 1
    else:
        contador0 += 1
resultados['ganados'].append(contador1)
resultados['perdidos'].append(contador0)
contador0 = 0
contador1 = 0

indice = np.arange(len(nombres))
 
## Se crean las primeras barras
plt.bar(indice, resultados['ganados'], label='Ganados')
 
## Se crean las segundas barras y se apilan sobre las primeras
plt.bar(indice, resultados['perdidos'], label='Perdidos',  bottom=resultados['ganados'])
 
plt.xticks(indice, nombres)
plt.ylabel("Partidos")
plt.xlabel("Equipos")
plt.title('Resultado de partidos')
plt.legend()
 
plt.show()