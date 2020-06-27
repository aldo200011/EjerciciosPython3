from EstudianteTarea4AldoCastillo import *

#def eliminarEstudiante(nombre: str):
#    estudiantes.delete_one({'Nombre': nombre})
#    result = estudiantes.find()

#    for e in result:
#        print(e)


estudiante_1 = Estudiante(
    nombre='Aldo',
    correo='aldo.example@email.com',
    contrasenia='0123456789'
)
estudiante_1.save()
result = estudiante_1.find_one('Aldo')
print(result)

estudiante_2 = Estudiante(
    nombre='Karla',
    correo='karla.example@email.com',
    contrasenia='0123456789'
)
estudiante_2.save()

estudiante_3 = Estudiante(
    nombre='Luis',
    correo='luis.example@email.com',
    contrasenia='9876543210'
)
estudiante_3.save()

estudiante_4 = Estudiante(
    nombre='Sofia',
    correo='sofia.example@email.com',
    contrasenia='9876543210'
)
estudiante_4.save()

estudiante_5 = Estudiante(
    nombre='Hector',
    correo='hector.example@email.com',
    contrasenia='3210456789'
)
estudiante_5.save()

estudiante_6 = Estudiante(
    nombre='Juan Carlos',
    correo='juan.carlos.example@email.com',
    contrasenia='7890123456'
)
result = estudiante_6.update_one('Aldo')
print(result,'\n')

estudiante_5.delete_one('Juan Carlos')
#eliminarEstudiante(nombre)