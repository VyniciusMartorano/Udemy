'''lista = [0,1,2,3,4,5]
iterar = iter(lista)
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))
print(next(iterar))'''
'''import sys

lista = list(range(10000000))
memoria_ocupada = sys.getsizeof(lista)
print(f'A variavel "lista" esta ocupando {memoria_ocupada} bytes de memoria no momento ')'''
from time import sleep
def gerador():
    for n in range(100):
        yield n
        sleep(0.1)
    return n
g = gerador()
for n in g:
    print(n)

