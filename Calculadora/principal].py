from Calculadora.funcionamento import *
from Calculadora.textos import *
from time import sleep
while True:
    cabeçalho('CALCULADORA PYTHON','blue')

    op = menu(['ADIÇÃO','SUBTRAÇÃO','MULTIPLICAÇÃO','DIVISÃO','ENCERRAR'])

    if op == 0:
        cabeçalho('ADIÇÃO','blue')
        n1 = leiafloat(input('n1: '))
        n2 = leiafloat(input('n2: '))
        sleep(1 / 2)
        print(f'{cor("white")}{n1} + {n2}')
        sleep(1)
        print(f'{cor("green")}Resultado: {somar(n1, n2)}{cor("stop")}')
    elif op == 1:
        cabeçalho('SUBTRAÇÃO','blue')
        n1 = leiafloat(input('n1: '))
        n2 = leiafloat(input('n2: '))
        sleep(1 / 2)
        print(f'{cor("white")}{n1} - {n2}')
        sleep(1)
        print(f'{cor("green")}Resultado: {subtração(n1,n2)}{cor("stop")}')
    elif op == 2:
        cabeçalho('MULTIPLICAÇÃO','blue')
        n1 = leiafloat(input('n1: '))
        n2 = leiafloat(input('n2: '))
        sleep(1 / 2)
        print(f'{cor("white")}{n1} * {n2}')
        sleep(1)
        print(f'{cor("green")}Resultado: {multiplicação(n1, n2)}{cor("stop")}')
    elif op == 3:
        cabeçalho('DIVISÃO', 'blue')
        n1 = leiafloat(input('n1: '))
        n2 = leiafloat(input('n2: '))
        sleep(1/2)
        print(f'{cor("white")}{n1} / {n2}')
        sleep(1)
        print(f'{cor("green")}Resultado: {divisão(n1, n2):.2f}{cor("stop")}')
    elif op == 4:
        print('Finalizando programa...')
        sleep(2)
        print('FIM!')
        break
