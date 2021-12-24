lista = [{'nome':'p1','preço':10},
         {'nome':'p1','preço':7},
         {'nome':'p1','preço':56},
         {'nome':'p1','preço':32},
         {'nome':'p1','preço':2}]

nova_lista = filter(lambda p: p['preço']>=10, lista)
for produto in nova_lista:
    print(produto)