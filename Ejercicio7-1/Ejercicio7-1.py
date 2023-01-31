import utils

print('Bienvenido a tu calculadora.')
print('Por favor selecciona la operacion que deseas ejecutar.')
op = input('Suma\nResta\nMultiplicacion\nDivision\n').lower()

while not op in ['suma', 'resta', 'multiplicacion', 'division']:
    print('Opcion invalida.')
    print('Por favor selecciona la operacion que deseas ejecutar.')
    op = input('Suma\nResta\nMultiplicacion\nDivision\n').lower()

num1 = input('Introduce el primer numero: ')
while not num1.isnumeric():
    num1 = input('Introduce el primer numero: ')
num2 = input('Introduce el segundo numero: ')
while not num2.isnumeric():
    num2 = input('Introduce el primer numero: ')
if op == "suma":
    print(utils.sumar(num1,num2))
elif op == "resta":
    print(utils.restar(num1,num2))
elif op == "multiplicacion":
    print(utils.multiplicar(num1,num2))
elif op == "division":
    print(utils.dividir(num1,num2))
