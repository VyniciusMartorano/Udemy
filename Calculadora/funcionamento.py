from Calculadora.textos import linha

def somar(n1 = 0, n2 = 0, n3 = 0):
    return n1 + n2 + n3

def subtração(n1 = 0, n2 = 0):
    return n1 - n2

def multiplicação(n1 = 1, n2 = 1, n3 = 1):
    return (n1 * n2 * n3)

def divisão(n1 = 0, n2 = 0):
    while True:
        try:
            resultado = n1 / n2
        except:
            print('\033[31mErro!digite valores válidos para a divisão.\033[m')
            try:
                n1 = float(input('n1: '))
                n2 = float(input('n2: '))
                resultado = n1 / n2
            except:
                continue
            else:
                return resultado
        else:
            return f'{resultado:.2f}'

def leiafloat(num):
    while True:
        try:
            num_float = float(num)
        except:
            print('\033[31mErro!Digite um numero válido\033[m')
            try:
                num_float = float(input('Digite um Valor: '))
            except:
                continue
            else:
                return num_float
        else:
            return num_float

def leiaint(num):
    while True:
        try:
            num_int = int(num)
        except:
            print('\033[31mErro!Digite um numero inteiro válido\033[m')
            try:
                num_int = int(input(f'{cor("white")}Digite um inteiro: {cor("stop")}'))
            except:
                continue
            else:
                return num_int
        else:
            return int(num_int)

def cor(escolha):
    if escolha == 'stop':
        return '\033[m'
    elif escolha == 'red':
        return '\033[31m'
    elif escolha == 'black':
        return '\033[1;30m'
    elif escolha == 'green':
        return '\033[1;32m'
    elif escolha == 'yellow':
        return '\033[1;33m'
    elif escolha == 'blue':
        return '\033[1;34m'
    elif escolha == 'cyan':
        return '\033[1;36m'
    elif escolha == 'white':
        return '\033[1;97m'

def menu(opção=[]):
    for pos, op in enumerate(opção):
        print(f'{cor("cyan")}{pos:-<6}{op}{cor("stop")}')
    tam = len(opção)
    while True:
        select = leiaint(input(f'{cor("white")}Sua opção: {cor("stop")}'))
        if select > tam or select < 0:
            print(f'{cor("red")}Opção invalida!{cor("stop")}')
            continue
        else:
            return select

def continuar():
    while True:
        resume = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        if resume == '' or resume not in 'SN' or resume.isdigit():
            print(f'{cor("red")}Opção inválida, digite apenas [S/N]{cor("stop")}')
            continue
        else:
            return resume




