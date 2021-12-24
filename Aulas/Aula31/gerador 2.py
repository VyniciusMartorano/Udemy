nome = 'vitor vynicius'
iterador = iter(nome)
try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass
print('CADE OS VALORES?')
for values in iterador:     # nao aparece mais porque esgotou
    print(values)           #a quantidade de iterações de "iterador"

    