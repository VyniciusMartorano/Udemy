lista = [
    ('chave1','valor1'),
    ('chave2','valor2')
]
d1 = {key.replace('1','.'): value for key, value in lista}
print(d1)