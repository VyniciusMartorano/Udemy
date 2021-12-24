from Aulas.Aula31.funcionamento import opções
dados = [{'nome':'Galaxy a10','preço':979.99},
         {'nome':'Galaxy a20','preço':1249.99},
         {'nome':'Galaxy a70','preço':[{'0':"4gb ram-----1989.99"},{'1':"6gb ram------R$2099.99"}]}]
carrinho = []
print(f'{"LOJINHA GUANABARA":^50}')
print('Aparelhos disponiveis para compra:')

for pos, elem in enumerate(dados):
    print(f'{pos}--->{elem["nome"]:>25}')
print('-=-'*13)


