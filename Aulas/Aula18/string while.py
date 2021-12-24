cont = 0
frase = 'o rato roeu a roupa do rei de roma'
tam = len(frase)
novastring = ''
while cont < tam:
    letra = frase[cont]
    if letra == 'r':
        novastring += 'R'
    else:
        novastring += letra
    cont += 1
print(novastring)