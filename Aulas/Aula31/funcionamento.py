def opções(estoque,carrinho=[]):
    opção = int(input('Digite o numero da sua opção: '))
    if opção == 1 or 2:
        print(f'Você selecionou o aparelho:'
              f' {estoque[opção]["nome"]}, preços:')
        for value in estoque[opção]['preço']:
            for key, itens in value.items():
                print(f'{key}--{itens}')
    seleção = str(input('Deseja adicionar algo ao carrinho?[999-->skip] '))
    if seleção == '999':
        print('voltando ao menu principal...')
    else:
        carrinho.append(estoque[opção]["preço"])
        print(carrinho)
dados = [{'nome':'Galaxy a10','preço':979.99},
         {'nome':'Galaxy a20','preço':[{'0':"4gb ram------R$1299.99"},{'1':"6gb ram------R$1499.99"}]},
         {'nome':'Galaxy a70','preço':{'0':"4gb ram------R$1989.99"},{'1':"6gb ram------R$2099.99"}]

opções(dados)