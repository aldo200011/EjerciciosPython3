from EstudianteTarea3AldoCastillo import *
import shelve
import pickle

estudiantesS = []
estudiantesP = []

def guardarEstudianteS(estudiante: Estudiante):
    with shelve.open('studentsS.db') as shelf:
        estudiantesS.append(estudiante)
        shelf[estudiante.getNombre()] = estudiante


def leerEstudiantesS():
    with shelve.open('studentsS.db') as shelf:
        es = [e for e in shelf]
        print(es)


def actualizarEstudianteS(estudiante: Estudiante, posicion: int):
    est: Estudiante =  estudiantesS[posicion]
    estudiantesS.pop(posicion)
    estudiantesS.insert(posicion, estudiante)

    with shelve.open('studentsS.db') as shelf:
        shelf.pop(est.getNombre())
        shelf[estudiante.getNombre()] = estudiante


def guardarEstudianteP(estudiante: Estudiante):
    file = open('studentsP.db', 'wb')
    estudiantesP.append(estudiante)
    p = pickle.Pickler(file)
    p.dump(estudiantesP)
    file.close()


def leerEstudiantesP():
    file = open('studentsP.db', 'rb')
    unpickler = pickle.Unpickler(file)
    estudiantesP = unpickler.load()
    for i in estudiantesP:
        print(i)


def actualizarEstudianteP(estudiante: Estudiante, posicion):
    estudiantesP.pop(posicion)
    estudiantesP.insert(posicion, estudiante)
    file = open('studentsP.db', 'wb')
    p = pickle.Pickler(file)
    p.dump(estudiantesP)
    file.close()


e1 = Estudiante('Aldo', 'aldo.example@email.com', '123456')
e2 = Estudiante('Karla', 'karla.example@email.com', '456789')
e3 = Estudiante('Luis', 'luis.example@email.com', '987654')
e4 = Estudiante('Sofia', 'sofia.example@email.com', '654321')
e5 = Estudiante('Hector', 'hector.example@email.com', '321456')

guardarEstudianteS(e1)
guardarEstudianteS(e2)
guardarEstudianteS(e3)
guardarEstudianteS(e4)
guardarEstudianteS(e5)
guardarEstudianteP(e1)
guardarEstudianteP(e2)
guardarEstudianteP(e3)
guardarEstudianteP(e4)
guardarEstudianteP(e5)
leerEstudiantesS()
leerEstudiantesP()

e6 = Estudiante('Juan Carlos', 'juan.carlos.example@email.com', '789123')
posicion = 0

actualizarEstudianteS(e6, posicion)
actualizarEstudianteP(e6, posicion)
leerEstudiantesS()
leerEstudiantesP()
