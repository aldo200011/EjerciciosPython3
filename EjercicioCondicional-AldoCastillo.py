def numeroPositivoNegativo(numero):
    if numero > 0:
        print("Es un numero positivo")
    elif numero < 0:
        print("Es un numero negativo")
    else:
        print("El numero es 0")


numero = int(input("Introduce un numero: "))
numeroPositivoNegativo(numero)

def numeroParImpar(numero):
    if numero % 2 == 0:
        print("Es un numero par")
    else:
        print("Es un numero impar")


numero = int(input("Introduce un numero: "))
numeroParImpar(numero)

def numeroPrimo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True


numero = int(input("Introduce un numero: "))
result = numeroPrimo(numero)
print(result)

def anioBisiesto(anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        print("Es un anio bisiesto")
    else:
        print("No es un anio bisiesto")


anio = int(input("Introduce un anio: "))
anioBisiesto(anio)