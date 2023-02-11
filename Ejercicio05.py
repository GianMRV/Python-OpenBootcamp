# Funcion para verificar si es bisiesto.
def is_leap_year(year):
    if int(year) % 4 == 0:
        print('El año ' + str(year) + ' es bisiesto.')
    else:
        print('El año ' + str(year) + ' no es bisiesto.')
        
# Validacion de datos.
while True:
    year = input('Por favor, ingresa el año que deseas consultar: ')
    try:
        while int(year) < 0:
            print('Ingresaste un valor incorrecto. Por favor, intentalo de nuevo.')
            year = input('Por favor, ingresa el año que deseas consultar: ')
        break
    except:
        print('Ingresaste un valor incorrecto. Por favor, intentalo de nuevo.')

is_leap_year(year)