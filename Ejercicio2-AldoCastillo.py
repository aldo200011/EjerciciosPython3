import re

def regex(cadena):
    patron1 = '[^A-Za-z][0-9@$?¡\-_]'
    patron2 = '^[0-9]*$'
    patron3 = '^[A-Z]*$'
    patron4 = '^[a-z]*$'
    patron5 = '[^0-9][A-Za-z@$?¡\-_]'
    er1 = re.match(patron1, str(cadena))
    er2 = re.match(patron2, str(cadena))
    er3 = re.match(patron3, str(cadena))
    er4 = re.match(patron4, str(cadena))
    er5 = re.match(patron5, str(cadena))

    if er1:
        print("La cadena no tiene letras")
    elif er2:
        print("La cadena solo tiene numeros")
    elif er3:
        print("La cadena solo tiene letras mayúsculas")
    elif er4:
        print("La cadena solo tiene letras minúsculas")
    elif er5:
        print("La cadena no tiene números")
    else:
        print("Cadena no válida")


cadena = input("Introduce una cadena de texto: ")
regex(cadena)