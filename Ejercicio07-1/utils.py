def sumar(a,b):
    return float(a)+float(b)
def restar(a,b):
    return float(a)-float(b)
def multiplicar(a,b):
    return float(a)*float(b)
def dividir(a,b):
    try:
        return float(a)/float(b)
    except ZeroDivisionError:
        print('ERROR. No se puede dividir entre cero')
