#sets sao ulteis para remover elementos duplicados de uma lista
# add (adiciona), update(atualiza), clear,discard(limpa)
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
#symmetric_difference ^ (elementos que estao nos dois sets, mas nao em ambos

'''l1 = [1,2,3,4,4,4,4,4,6,7,9,'vitor','joao','vitor','joao']
print(l1)
l1 = set(l1)
print(l1)
l1 = list(l1)
print(l1)'''

s1 = {1,2,3,4,5,5,6}
s2 = {3,4,5,6,7,7,7,7}
s3 = s1 | s2    #juntar s1 e s2
print(s3)


