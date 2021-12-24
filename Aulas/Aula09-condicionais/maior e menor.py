maior = menor = 0
lista = []
for c in range(0,4):
    n = float(input('n1: '))
    lista.append(n)
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Numeros digitados: {lista}')
print(f'maior: {maior}')
print(f'menor: {menor}')
