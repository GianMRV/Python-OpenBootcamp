# Creacion de la clase
class Vehiculo():
    color = "negro"
    ruedas = 4
    puertas = 2

# Creacion de la clase heredada
class Coche(Vehiculo):
    velocidad = 200
    cilindrada = 16

# Creacion del objeto
carro = Coche()
print('El color del carro es', carro.color)
print('Tiene ', str(carro.ruedas), 'ruedas y', str(carro.puertas), 'puertas.')
print('Alcanza una velocidad de', str(carro.velocidad))
print('Y tiene', str(carro.cilindrada), 'cilindros.')