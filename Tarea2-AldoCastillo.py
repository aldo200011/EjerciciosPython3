import re

def validarCorreo(correo):
    patron = '[a-zA-Z]+@[a-zA-Z]+[.][a-zA-Z]+[.][a-zA-Z]+$'
    ra = re.match(patron, str(correo))

    if ra:
        print(f'El correo {correo} es valido')
    else:
        print('Correo no valido')


def validarNumeroTelefonico(numeroTelefonico):
    patron = '[(][0-9]{2,3}[)]\s[0-9]{3,4}[\s|-][0-9]{3,4}$'
    ra = re.match(patron, str(numeroTelefonico))

    if ra:
        print(f'El numero {numeroTelefonico} es valido')
    else:
        print('Marcacion incorrecta')


def validarRFCCurp(rfc, curp):
    patron = '[A-Z][AEIOU][A-Z]{2}[0-9]{6}[A-Z0-9]{3}$'
    ra = re.match(patron, str(rfc))
    patron = '[A-Z]{4}[0-9]{6}[H|M][A-Z]{2}[^AEIOU]{3}[09|A-Z]{2}$'
    rb = re.match(patron, str(curp))

    if ra and rb:
        print(f'RFC {rfc} y CURP {curp} validos')
    elif ra:
        print('CURP no valido')
    elif rb:
        print('RFC no valido')

validarCorreo('aldo@padts.com.mx')
validarNumeroTelefonico('(33) 1437 1583')
validarRFCCurp('CACX930711R45', 'CXCA930711HCSSRL09')