nome = str(input('Digite seu nome: ')).strip()
tam = len(nome)
if tam<=4:
    print(f'{nome} Seu nome tem apenas {tam} Letras e é curto demais')
if 5<=tam<=6:
    print(f'{nome} Seu nome tem apenas {tam} Letras, Seu nome é Normal.')
if tam>6:
    print(f'{nome} Seu nome tem apenas {tam} Letras e é grande demais')