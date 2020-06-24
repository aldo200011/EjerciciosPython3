def ordenamientoBurbuja(list):
    for numero in range(len(list) - 1, 0, -1):
        for i in range(numero):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp


list = [5, 9, 3, 1, 2, 8, 4, 7, 6]
print(list)
ordenamientoBurbuja(list)
print(list)
