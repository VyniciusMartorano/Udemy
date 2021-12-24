lista = [1,2,3,4,5,6]
duplicar = [v * 3 for v in lista]
total = 0
for num in duplicar:
    total += num
ex1 = [lista[0:5] for v in range(3)]
for k,v in enumerate(ex1):
    ex1[k][3] = 'vitor'
print(ex1)
