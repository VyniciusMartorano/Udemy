#formula de bhaskara
from math import sqrt
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

#delta = (b**2)+(- 4 * a * c)
delta = (b**2) - 4 * a * c
if delta<0:
    print('Impossivel calcular!')
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'Resultado:\nDelta: {delta}\nX1: {x1}\nX2: {x2}')
    print(f'Solução=({x1},{x2})')