def ordenamientoBurbuja(list):
    for numero in range(len(list) - 1, 0, -1):
        for i in range(numero):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp


i = 1
lista = list()
while i == 1:
    while True:
        try:
            numero = int(input('Introduce un numero: '))
            lista.append(numero)
            break
        except ValueError:
            print('Debes ingresar un número entero')

    while True:
        try:
            i = int(input('Deseas introducir otro numero? Presiona [1] para insertar otro numero '))
            break
        except ValueError:
            print('Debes ingresar un número entero')


#list = [5, 9, 3, 1, 2, 8, 4, 7, 6]
print(lista)
ordenamientoBurbuja(lista)
print(lista)
