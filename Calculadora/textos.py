def cabeçalho(msg,color='\033[m'):
    from Calculadora.funcionamento import cor
    print(f'{cor(color)}='*60)
    print(f'{msg:^60}')
    print('=' * 60)

def linha(tam):
    print('-'*60)

