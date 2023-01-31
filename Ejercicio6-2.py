# Creacion de la clase
class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

# Verificacion de la entrada del usuario
nombre = ""
nota = ""
while not nombre.isalpha():
    nombre = (input('Ingrese el nombre del alumno: '))
while not nota.isnumeric() or int(nota) > 20:
    nota = (input('Ingrese la calificación: '))

alguien = Alumno(nombre,nota)

# Verificacion de aprobacion
if int(alguien.nota) < 10:
    print('El estudiante', alguien.nombre.capitalize(), 'con', alguien.nota, 'puntos, no aprueba.')
else:
    print('El estudiante', alguien.nombre.capitalize(), 'con', alguien.nota, 'puntos, aprueba.')