lista = []
for rep in range(3):
    a = input('Num: ')
    if a.isalpha():
        n = [str(a)]
    else:
        n = [int(c) for c in a]
    lista.append(n)
print(lista)