from Aulas.Aula31.regradetres import regra_de_tres
flamengo = palmeiras = atletico_mg = maior = menor = 0
times = [flamengo,atletico_mg,palmeiras]
total = 0
continuar = 'S'
lista = ['Flamengo','Palmeiras','Atletico_mg']
while continuar == 'S':
    print('MELHOR TIME DO BRASIL')
    for pos, time in enumerate(lista):
        print(f'{pos}{"":-^15}{time}')
    while True:
        try:
            voto = int(input('Seu voto: '))
        except:
            print('Numero invalido')
        else:
            break
            pass
    total += 1
    if voto == 0:
        flamengo += 1
    elif voto == 1:
        palmeiras += 1
    elif voto == 2:
        atletico_mg += 1
    continuar = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for pos, time in enumerate(times):
    if pos == 0:
        maior = time
        menor = time
    else:
        if time > maior:
            maior = time
        if time < menor:
            menor = time

print('='*40)
print(f'Flamengo: {regra_de_tres(total,flamengo)}\n'          
    f'Palmeiras: {regra_de_tres(total,palmeiras)}\n'
    f'Atletico MG: {regra_de_tres(total,atletico_mg)}\n'
    f'Total de votos: {total}\n'
    f'Melhor time do brasil: {maior}')



