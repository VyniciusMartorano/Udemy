from itertools import combinations, permutations, product

pessoas = ['andre','vitor','joao','larissa','leticia']

'''for grupo in combinations(pessoas,2):
    print(grupo)'''   #combinaçoes de 2 pessoas possiveis no grupo pessoas

'''for grupo in permutations(pessoas,2):   #tem repetição de combinação
    print(grupo)'''
for grupo in product(pessoas, repeat=2):    #ordem importa
    print(grupo)
