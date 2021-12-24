#mult = lambda x, y: x * y   #x e y sao argumentos
#print(mult(3,4))

lista = [['p1',16],
         ['p2',13],
         ['p3',7],
         ['p4',25],
         ['p5',16]
         ]


lista.sort(key = lambda item: item[0],) #ordenar em ordem crescente usando a função anonima lambda
print(lista)                            #que seleciona o argumento 1 como parametro
