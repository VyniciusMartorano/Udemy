
dados = ['vynicius26', 'guanabara']
while True:
    login = str(input('Login: ')).strip()
    senha = str(input('Senha: ')).strip()
    if login == dados[0] and senha == dados[1]:
        print('login.txt bem sucedido!')
        break
    else:
      print('Login ou senha incorretos!')