from mongoengine import *
from pymongo import MongoClient

connect('padts', host='localhost', port=27017)

class Estudiante(Document):
    nombre = StringField(required=True, max_length=20)
    correo = StringField(required=True, max_length=20)
    contrasenia = StringField(required=True, min_length=10)
    __cliente = MongoClient()
    __db = __cliente['padts']
    __estudiantes = __db['estudiantes']

    def save(
        self,
        force_insert=False,
        validate=True,
        clean=True,
        write_concern=None,
        cascade=None,
        cascade_kwargs=None,
        _refs=None,
        save_condition=None,
        signal_kwargs=None,
        **kwargs
    ):
        self.__estudiantes.insert_one({'Nombre': self.nombre,
                                       'Correo': self.correo,
                                       'Contraseña': self.contrasenia})


    def find_one(self, nombre: str):
        obj = Estudiante.objects(nombre = nombre)[0]
        return obj


    def update_one(self, nombre: str):
        self.__estudiantes.update_one({'Nombre': nombre},
                                      {'$set': {'Nombre': self.nombre,
                                                'Correo': self.correo,
                                                'Contraseña': self.contrasenia}})
        filtro = self.__estudiantes.find({'Nombre': self.nombre})

        for e in filtro:
            return e


    def delete_one(self, nombre: str):
        self.__estudiantes.delete_one({'Nombre': nombre})
        filtro = self.__estudiantes.find()

        for e in filtro:
            print(e)


    def __str__(self):
        return f'Nombre: {self.nombre}\n' \
                f' Correo: {self.correo}\n' \
                f' Contraseña: {self.contrasenia}\n'