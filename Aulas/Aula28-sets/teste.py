l1 = [1,2,3,4,5,6,7]

ex1 = [variavel for variavel in l1]
ex2 = [v*2 for v in l1]
#multiplicar cada valor de l1 por 2
l2 = ['paulo','maria','martorano']

ex3 = [v.replace('a','@') for v in l2]
tupla = (('chave','valor'),('chave2','valor2'))
ex4 = [(v, k) for k, v in tupla]
ex4 = dict(ex4)
print(ex4)