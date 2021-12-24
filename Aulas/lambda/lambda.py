lista = [['p1',16],
         ['p2',13],
         ['p3',7],
         ['p4',25],
         ['p5',8]
         ]
lista.sort(key= lambda x: x[1], reverse=True)

maiores = filter(lambda x: x[1]>10, lista)

lista_atu = [elem for elem in maiores]
lista_atu.sort(key=lambda x: x[0])
print(lista_atu)
