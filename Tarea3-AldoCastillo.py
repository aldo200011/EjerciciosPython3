from StudentIOTarea3 import *

estudiantes = []

def guardarEstudiante(estudiante = Estudiante):
    file = open('students.db', 'a+')
    file.write(estudiante.__str__())
    file.close()
    estudiantes.append(estudiante.__str__())


def leerEstudiantes():
    file = open('students.db', 'r+')
    print(file.read())
    file.close()


def actualizarEstudiante(estudiante = Estudiante, posicion = int):
    estudiantes.pop(posicion)
    estudiantes.insert(posicion, estudiante.__str__())
    file = open('students.db', 'w+')

    for e in estudiantes:
        file.write(e)


    file.close()


e1 = Estudiante('Aldo', 'aldo.example@email.com', '123456')
e2 = Estudiante('Karla', 'karla.example@email.com', '456789')
e3 = Estudiante('Luis', 'luis.example@email.com', '987654')
e4 = Estudiante('Sofia', 'sofia.example@email.com', '654321')
e5 = Estudiante('Hector', 'hector.example@email.com', '321456')

guardarEstudiante(e1)
guardarEstudiante(e2)
guardarEstudiante(e3)
guardarEstudiante(e4)
guardarEstudiante(e5)
leerEstudiantes()

e1.setNombre('Juan Carlos')
e1.setCorreo('juan.carlos.example@email.com')
e1.setContrasenia('789123')
posicion = 0

actualizarEstudiante(e1, posicion)
leerEstudiantes()