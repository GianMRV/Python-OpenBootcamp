# Importar el modulo time
import time

# Crear la funcion para calcular el tiempo restante
def calcula_tiempo(horas, minutos, segundos):
    res_h = 6 - int(horas)
    res_m = 60 - int(minutos)
    res_s = 60 - int(segundos)
    return print('Te restan', res_h, 'horas,', res_m, 'minutos y', res_s, 'segundos.')

# Solicitar la hora del sistema
hora = time.strftime("%I")
min = time.strftime("%M")
seg = time.strftime("%S")

# Mostrar mensaje o calcular tiempo restante
if int(hora) > 7:
    print('Ya es hora de irte a casa.')
else:
    calcula_tiempo(hora,min,seg)