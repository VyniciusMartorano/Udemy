def duplicados(lista):
    checados = set()
    primeiro_duplicado = -1
    for numero in lista:
        if numero in checados:
            primeiro_duplicado = numero
            break
        checados.add(numero)
    return primeiro_duplicado


lista = [1,2,2,2,3,4,5,5,5]

print(duplicados(lista))

