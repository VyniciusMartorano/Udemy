num = input('Digite um numero inteiro: ')
try:
    n = int(num)
except:
    print('ERRO!digite um numero inteiro válido.')
else:
    print(f'Você digitou o numero {n}')