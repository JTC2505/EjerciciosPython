def stringHour(hora):
    stringH = ''
    stringM = '00'
    stringHourComplete = ''
    if(hora < 10):
        stringH = '0' + str(hora)
    else:
        stringH = str(hora)
    if(hora == 24):
        stringH = '23'
        stringM = '59'
    stringHourComplete = stringH + ':' + stringM
    return stringHourComplete