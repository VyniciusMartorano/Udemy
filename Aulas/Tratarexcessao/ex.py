def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except (ValueError):
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
while True:
    numero = converte_numero(input('Numero: '))
    if numero is None:
        print('isso nao é numero')
    else:
        print(numero * 2)