from itertools import count

contador = count(start=5,step=0.1)     #step = passo
for valor in contador:
    print(round(valor,1))           #round arredonda o numero
    if valor > 10:
        break