d1 = {
    'chave1':'valor',
    'chave2':'outro valor',
    'chave3':'terceiro valor'
}
for key, value in d1.items():
    print(f'the key is \033[31m{key}\033[m and value is \033[33m{value}\033[m')
