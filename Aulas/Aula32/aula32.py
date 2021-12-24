'''
zip - Unindo iteraveis
zip_longest - Itertools
'''
#Codigo
from itertools import zip_longest, count

cidades = ['São Paulo', 'Belo horizonte', 'Salvador']

#codigo

estados = ['SP','MG','Bahia']
indice = count()

cidades_estados = zip(indice, estados, cidades)

for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)





'''cidades_estados = zip(cidades, estados)
print(list(cidades_estados))


for item in cidades_estados:
    print(item)'''

