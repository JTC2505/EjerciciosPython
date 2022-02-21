# En el Hospital "La mejor Salud", para el control del contagio del COVID se ha implementado la práctica que por cada paciente se registre cada hora la temperatura. 
# Luego, por cada paciente se genera una gráfica diaria de cómo se ha comportado la misma. 
# Haga el programa que permita registrar las temperaturas que se han tomado cada hora (de horas a 23:59 horas -o 24:00) que genere la gráfica correspondiente. 
# Deberá también ingresarse el número de pacientes a quienes se les registrará su temperatura y se les calculará su gráfica de comportamiento de temperatura corporal.
from GraphTempModulo import *
import matplotlib.pyplot as plt
import numpy as np

temperaturaXhora = []
temperaturaXpersona = []
temperaturas = []
continuar = 1
hora = 0
contador = 1
horas = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00','23:59']
colores = ['blue','green','red','cyan','magenta','yellow','black','white','blue','green','red','cyan','magenta','yellow','black','white','blue','green','red','cyan','magenta','yellow','black','white']
print('Bienvenido/a')
NoPacientes = int(input('Por favor ingrese la cantidad de pacientes a los que se les tomara la temperatura: '))
while hora <= 24:
    print('\nSon las ' + stringHour(hora) +' horas, escriba las temperatura de los pascientes: ')
    while contador <= NoPacientes:
        temperaturas.append(float(input('\nPor favor ingrese la temperatura del paciente ' + str(contador) + ': ')))
        contador += 1
    temperaturaXhora.append(temperaturas)
    hora += 1
    contador = 1
    temperaturas = []

input('\nPara ver las graficas correspondientes a la temperatura presione enter...')

contador = 0
listdynamic = []
for i in range(0, NoPacientes):
    for x in temperaturaXhora:
        listdynamic.append(x[contador])
    temperaturaXpersona.append(listdynamic)
    listdynamic = []
    contador += 1

fig = plt.figure(figsize=(22,8))
fig.tight_layout()
for i in range(0, len(temperaturaXpersona)):
    ax = plt.subplot(2,4,i+1)
    ax.bar(horas, temperaturaXpersona[i],color=colores[i])
    ax.set_ylabel('temperatura')
    ax.set_title('Paciente ' + str(i + 1))
    plt.xticks(rotation=90)
plt.show()