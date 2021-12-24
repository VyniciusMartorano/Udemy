carrinho = []
carrinho.append(('produto 1', 10))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 30))
produto, preço = carrinho[0]
print(f'{produto}---R${preço}')
total = sum([float(y) for x, y in carrinho])
print(total)
