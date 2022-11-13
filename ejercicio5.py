"""
Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

"""
bisiesto = lambda numero : "Es bisiesto" if (numero % 4 == 0 and numero % 100 != 0 or numero % 400 == 0) else "No es bisiesto"

print ( bisiesto (int(input('Introduzca el año: '))))



