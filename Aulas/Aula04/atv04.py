nome = str(input('Nome: '))
idade = int(input('Idade: '))
altura = float(input('Altura: '))
print(nome,type(nome))
print(idade,type(idade))
print(altura,type(altura))
print(f'É maior de idade?{bool(idade<=18)}')