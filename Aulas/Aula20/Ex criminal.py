'''Utilizando listas faça um programa que faça 5 perguntas
 para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima ?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir
uma classificação sobre a participação
da pessoa no crime. Se a pessoa
responder positivamente a 2
questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
 e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

def formulario(resultado=''):
    print('\033[31m-=-'*15)
    print(f'{"INTERROGATORIO CRIMINAL":^45}')
    print('\033[31m-=-\033[m'*15)
    p1 = str(input('Telefonou para a vítima?[S/N] ')).strip().upper()[0]
    p2 = str(input('Esteve no local do crime?[S/N] ')).strip().upper()[0]
    p3 = str(input('Mora perto da vitima?[S/N] ')).strip().upper()[0]
    p4 = str(input('Devia para a vitima?[S/N] ')).strip().upper()[0]
    p5 = str(input('Ja trabalhou com a vitima?[S/N] ')).strip().upper()[0]
    contador = 0
    if p1 == 'S':
        contador += 1
    if p2 == 'S':
        contador += 1
    if p3 == 'S':
        contador += 1
    if p4 == 'S':
        contador += 1
    if p5 == 'S':
        contador += 1
    #CLASSIFICAÇÃO
    if contador == 2:
        resultado = '\033[1;100mA pessoa interrogada foi classificada como Suspeito\033[m'
    elif 3<=contador<=4:
        resultado = '\033[1;33mA pessoa interrogada foi classificada como Cúmplice.\033[m'
    elif contador == 5:
        resultado = '\033[1;31mA pessoa interrogada foi classificada como Assassino.\033[m'
    elif contador<2:
        resultado = '\033[1;92mA pessoa interrogada foi classificada como Inocente.\033[m'
    print()
    return resultado


print(formulario())





