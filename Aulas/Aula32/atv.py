lista1 = [1,2,3,4,5,6,7,8]
lista2 = [1,2,3,4,5,6,7,8]
resultado = []
if len(lista1)>len(lista2):
    for i in range(len(lista2)):
        resultado.append(lista1[i] + lista2[i])
    print(resultado)
elif len(lista2)>len(lista1):
    for i in range(len(lista1)):
        resultado.append(lista1[i] + lista2[i])
    print(resultado)
else:
    for i in range(len(lista1)):
        resultado.append(lista1[i] + lista2[i])
    print(resultado)


