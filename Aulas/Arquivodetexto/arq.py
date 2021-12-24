'''with open('arquivo.txt','r') as file:
    #file.write('Linha1\n')
    #file.write('Linha2\n')
    #file.write('Linha3\n')
    #file.seek(0,0)
    print(file.read())'''
with open('arquivo.txt','a+') as file:
    file.write('Outra linha\n')
    file.seek(0,0)
    print(file.read())

