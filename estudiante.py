class Estudiante():
    __nombre: str
    __correo: str
    __contrasenia: str

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


    def __str__(self):
        return f'Nombre: {self.__nombre}\n' \
               f' Correo: {self.__correo}\n' \
               f' Contraseña: {self.__contrasenia}\n'