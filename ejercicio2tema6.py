"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista
pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante redu
"""
from functools import reduce
def pares(numero):
    if numero % 2 == 0:
        return True
    return False

def suma(a,b):
    return a + b

lista = [2,5,6,4,3,7,9,8,1]

pares = filter(pares, lista)
resultadosuma = reduce(suma, lista)

print(list(pares))
print( resultadosuma)

