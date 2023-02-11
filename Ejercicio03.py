def request():
    weight = input('Por favor, ingresa tu peso: ')
    height = input('Por favor, ingresa tu altura: ')
    return [weight,height]

while True:
    data = request()
    weight = data[0]
    height = data[1]
    try:
        while (float(weight) < 0) or (float(weight) > 350) or (float(height) < 0) or (float(height) > 350):
            print('Ingresaste un valor incorrecto. Por favor, intentalo de nuevo.')
            data = request()
            weight = data[0]
            height = data[1]
        break
    except ValueError:
        print('Ingresaste un valor incorrecto. Por favor, intentalo de nuevo.')

imc = float(weight)/(float(height)**2)
print('Tu IMC es ' + str("{:.2f}".format(imc)) + ' kg/m2.') #format limita el numero de decimales. En este caso 2.

