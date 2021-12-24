def alternativas(a,b,c,d,e,respcert=''):
    if respcert == '' or respcert not in 'abcdeABCDE':
        return '\033[31mERRO!Verifiquei se o campo esta\n' \
               'preenchido com a,b,c,d ou e.\033[m'

    else:
        lista = a, b, c, d, e
        elem = '[ A ]','[ B ]','[ C ]','[ D ]','[ E ]'
        correta = respcert
        print()
        print('ALTERNATIVAS:')
        for pos, alter in enumerate(lista):
            print(f'{elem[pos]} {alter}')
        resposta = str(input('Resposta: ')).strip().lower()
        while resposta not in 'abcdeABCDE' or resposta == '':
            print('\033[31mAlternativa inválida!\033[m')
            resposta = str(input('Resposta: ')).strip().lower()
        if correta.lower() == resposta.lower():
            return '\033[32mResposta Certa.\033[m'
        else:
            return f'\033[31mResposta Errada.\nAlternativa correta\033[m:\033[1;32m {correta.upper()}\033[m'


def enunciado(numquest,msg):
    print('\033[33m-'*60)
    cont = 0
    print(f'{f"QUESTÃO {numquest}":^60}')
    print('-' * 60)
    for palavras in msg:
        cont += 1
        if cont < 56:
            print(palavras,end='')
        else:
            cont = 0
            print(palavras)
    print('\033[m')


def login():
    dados = {'user':'vynicius26','password':'Felipebia123'}
    print('\033[33m-' * 45, '\033[m')
    cadastrar = str(input('You have Registration?[Y/N] ')).strip().upper()[0]
    while cadastrar not in 'YN':
        cadastrar = str(input('You have Registration?[Y/N] ')).strip().upper()[0]
    if cadastrar == 'N':
        print('\033[33m-' * 45, '\033[m')
        print('Register in the system')
        print()
        dados['user'] = str(input('Username: ')).strip()
        dados['password'] = str(input('Password: ')).strip()
        confirmarsenha = str(input('Repeat Password: ')).strip()
        while confirmarsenha != dados['password']:
            print('ERROR!Passwords do not match.')
            confirmarsenha = str(input('Repeat Password: ')).strip()
        print('Registration performed successfully!')
        print('\033[33m-'*45,'\033[m')
        print('LOGIN')
        print()
        login = str(input('Username: ')).strip()
        password = str(input('Password: ')).strip()
        while login != dados['user']:
            print('ERROR!Incorrect login.txt.')
            login = str(input('Username: ')).strip()
        while password != dados['password']:
            print('ERROR!Incorrect password.')
            password = str(input('Password: ')).strip()
        print('Login is sucessfully!')
    else:
        login = str(input('Username: ')).strip()
        password = str(input('Password: ')).strip()
        while login != dados['user']:
            print('ERROR!Incorrect login.txt.')
            login = str(input('Username: ')).strip()
        while password != dados['password']:
            print('ERROR!Incorrect password.')
            password = str(input('Password: ')).strip()
        print('Login is sucessfully!')







