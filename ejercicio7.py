"""
En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
 que tenga como atributos su nombre y su nota.
 Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y
  mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Alumno():
    nombre = None
    nota = None

    def __init__(self, pnombre, pnota):
        self.nombre = pnombre
        self.nota = int(pnota)

    def calcularcalificacion(self):
        return "Aprobado" if self.nota >= 5 else "Suspenso"


nombre = input("Introduzca nombre del alumno: ")
nota = input("Indique nota del alumno: ")

alumno = Alumno(nombre, nota)

print("El alumno",alumno.nombre, "ha obtenido la calificación de", alumno.calcularcalificacion())



