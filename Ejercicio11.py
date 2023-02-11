import sqlite3

con = sqlite3.connect('Ejercicio11.db')

cursor = con.cursor()

cursor.execute('CREATE TABLE Alumnos (id INT, nombre text, apellido text)')

students = [
    (1, 'Jose', 'Martínez'),
    (2, 'Luis', 'Jimenez'),
    (3, 'Valeria', 'Quintana'),
    (4, 'Valentina', 'Goncalvez'),
    (5, 'Peter', 'Paredes'),
    (6, 'Juan', 'Domínguez'),
    (7, 'Francisco', 'Suárez'),
    (8, 'María', 'Rodríguez'),
]
cursor.executemany('INSERT INTO Alumnos VALUES (?,?,?)', students)

rows = cursor.execute("SELECT * FROM Alumnos WHERE nombre='Jose'")
for row in rows:
    print(row)

con.close()