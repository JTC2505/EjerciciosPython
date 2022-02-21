def Noequipo(equipo, nombres):
    resultado = 0
    if(nombres[0] == equipo):
        resultado = 1
    elif(nombres[1] == equipo):
        resultado = 2
    elif(nombres[2] == equipo):
        resultado = 3
    elif(nombres[3] == equipo):
        resultado = 4
    return resultado

def equipoG(equipo, partidosE1, partidosE2, partidosE3, partidosE4):
    if(equipo == 1):
        partidosE1.append(1)
    elif(equipo == 2):
        partidosE2.append(1)
    elif(equipo == 3):
        partidosE3.append(1)
    elif(equipo == 4):
        partidosE4.append(1)

def equipoP(equipo, partidosE1, partidosE2, partidosE3, partidosE4):
    if(equipo == 1):
        partidosE1.append(0)
    elif(equipo == 2):
        partidosE2.append(0)
    elif(equipo == 3):
        partidosE3.append(0)
    elif(equipo == 4):
        partidosE4.append(0)
    