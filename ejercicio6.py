
"""FUNCIONES DE ORDEN SUPERIOR, creamos una lista, la procesamos y 
multiplicamos por 2 cada uno de sus elementos"""

def multiplicar(x):
    return x*2

def cuadrado (x):
    return x**2

def aplicar(datos):

    aux = []
    for n in datos:
        aux.append(function(n))
    return aux

##################################

numeros = [1,2,3]


r = aplicar(multiplicar, numeros)

print(r)