dados = []
cache = {}
cache['nome'] = 'vitor'
dados.append(cache.copy())
cache.clear()
cache['nome'] = 'josé'
dados.append(cache.copy())
cache.clear()
for value in dados:
    print(value['nome'])


