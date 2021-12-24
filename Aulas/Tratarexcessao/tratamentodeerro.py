try:
    print(a)
except (NameError) as erro:
    print(f'{erro} ')
except (IndentationError):
    print('Erro!')
else:
    print('Tudo certo')