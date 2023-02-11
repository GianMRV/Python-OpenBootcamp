# Entrada del usuario
list_countries = (input('Ingresa los paises que desees, separados por coma.\n').split(','))

countries = []
for i in list_countries:
    i = i.strip()                       # Eliminar los espacios iniciales y finales
    if not i.isalpha():                 # Eliminar elementos numericos o especiales
        continue
    countries.append(i.capitalize())
countries = sorted(set(countries))      # Eliminar elementos repetidos y ordenar alfabeticamente

print(countries)
