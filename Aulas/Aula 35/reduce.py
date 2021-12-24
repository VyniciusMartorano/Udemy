from functools import reduce

lista = [['p1',16],
         ['p2',13],
         ['p3',7],
         ['p4',25],
         ['p5',8]
         ]
soma_preços = reduce(lambda ac, p: p[1] + ac, lista, 0)
print(soma_preços)      #soma todos os elementos da lista
