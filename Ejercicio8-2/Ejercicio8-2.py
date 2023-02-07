import pickle

class Vehiculo():
    marca= 'Toyota'
    modelo= '15TH89'
    puertas= 4
    velocidad= '280 kph'

carro = Vehiculo()

file = open('Ejercicio8-2/Ejercicio8-2.pickle', 'wb')
pickle.dump(carro, file)