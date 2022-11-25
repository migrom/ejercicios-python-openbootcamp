"""
Crea un script que le pida al usuario una lista de países (separados por comas).
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
"""
from pprint import pprint
listausuario = input('Introduce una lista de paises separados por coma: ')


listapaises = listausuario.split(',')

listapaisesfinal = (pais for pais in listausuario.split(", "))

pprint(sorted(set(listapaisesfinal)))

