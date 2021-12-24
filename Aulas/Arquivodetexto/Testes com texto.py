file = open('abc.txt','w+')
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')
file.write('Linha4\n')
file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')
file.close()