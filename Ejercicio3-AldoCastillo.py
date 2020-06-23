import cmath

class Figura():
    _lado = 0

    def perimetro(self):
        pass


    def area(self):
        pass


class Rectangulo(Figura):
    __largo = 0
    __ancho = 0

    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho


    def perimetro(self):
        return (2 * self.__largo) + (2 * self.__ancho)


    def area(self):
        return self.__largo * self.__ancho


class Triangulo(Figura):
    def __init__(self, lado):
        self._lado = lado


    def perimetro(self):
        return 3 * self._lado


    def area(self):
        return (cmath.sqrt(3) / 4) * self._lado


class Estudiante():
    __nombre = ''
    __correo = ''
    __contrasenia = ''

    def __init__(self, nombre, correo, contrasenia):
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasenia = contrasenia


    def getNombre(self):
        return self.__nombre


    def setNombre(self, nombre):
        self.__nombre = nombre


    def getCorreo(self):
        return self.__correo


    def setCorreo(self, correo):
        self.__correo = correo


    def getContrasenia(self):
        return self.__contrasenia


    def setContrasenia(self, contrasenia):
        self.__contrasenia = contrasenia


if __name__ == '__main__':
    r = Rectangulo(5, 2.5)
    print(f'Perimetro del rectangulo: {r.perimetro()}')
    print(f'Area del rectangulo: {r.area()}\n')
    t = Triangulo(10)
    print(f'Perimetro del triangulo: {t.perimetro()}')
    print(f'Area del triangulo: {t.area()}\n')
    e = Estudiante('Aldo', 'aldo@example.com', '123456')
    print(f'Nombre del estudiante: {e.getNombre()}')
    print(f'Correo: {e.getCorreo()}')
    print(f'Contrasenia: {e.getContrasenia()}\n')
    e.setNombre('Luis')
    e.setCorreo('luis@example.com')
    e.setContrasenia('987654')
    print(f'Nombre del estudiante: {e.getNombre()}')
    print(f'Correo: {e.getCorreo()}')
    print(f'Contrasenia: {e.getContrasenia()}')
