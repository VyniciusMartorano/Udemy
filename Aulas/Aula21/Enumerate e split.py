string = 'O brasil é o pais do futebol, o brasil é penta.'
lista = string.split()
for elem in lista:
    print(f'A palavra {elem} apareceu {lista.count(elem)}x na frase')
