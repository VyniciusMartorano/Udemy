
hora = input('escolha um horario entre (0-23) : ')
if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Esse horario não está dentro de 0 à 23')
    else:
        if hora <= 11:
            print('Bom dia!')
        elif hora >= 11 and hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite')
else:
    print('Por favor digite um valor entre 0 e 23')