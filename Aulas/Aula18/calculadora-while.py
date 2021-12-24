from time import sleep
while True:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    operador = str(input('Qual operador(+,-,*,/)?' )).strip()
    sleep(1/4)
    print(f'Operador escolhido: {operador}')
    if operador == '+':
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif operador == '-':
        subtração = n1 - n2
        print(f'{n1} - {n2} = {subtração}')
    elif operador == '/':
        divisão = n1 / n2
        print(f'{n1} / {n2} = {divisão:.2f}')
    elif operador == '*':
        multiplicação = n1 * n2
        print(f'{n1} * {n2} = {multiplicação}')
    continuar = str(input('Quer continuar[S/N]?')).strip().upper()[0]
    print()
    sleep(1/4)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N]?')).strip().upper()[0]
        print()
    if continuar == 'N':
        sleep(1)
        break

print('Programa encerrado!')



