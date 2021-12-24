from time import sleep
from sys import getsizeof   #mostra a memoria que esta sendo usada
lista1 = [x for x in range(100000)]   #80094 bytes utilizados na memoria
lista2 = (x for x in range(100000))   #112 bytes utilizados na memoria
print(getsizeof(lista1))
print(getsizeof(lista2))

#for value in lista1:
#    print(value)