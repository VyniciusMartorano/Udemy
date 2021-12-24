from Aulas.miniprova.Perguntas import *
login()
msg = '(Enem/2018) Em Beirute, no Líbano,' \
      ' quando perguntado sobre onde se ' \
      'encontram os refugiados sírios, ' \
      'a resposta do homem é imediata: ' \
      '“em todos os lugares e em lugar nenhum”' \
      '. Andando ao acaso, não é raro ver, sob' \
      ' um prédio ou num canto de calçada, ao' \
      ' abrigo do vento, uma família refugiada' \
      ' em volta de uma refeição frugal posta ' \
      'sobre jornais como se fossem guardanapos. ' \
      'Também se vê de vez em quando uma tenda ' \
      'com a sigla ACNUR (Alto Comissariado das ' \
      'Nações Unidas para Refugiados), erguida ' \
      'em um dos raros terrenos vagos da capital.' \
      'O cenário descrito aponta para uma crise' \
      ' humanitária que é explicada pelo processo de:'

enunciado(1,msg)

print(alternativas('migração massiva de pessoas atingidas por catástrofe natural.',
    'hibridização cultural de grupos caracterizados por homogeneidade social.',
    'desmobilização voluntária de militantes cooptados por seitas extremistas.',
    'peregrinações religiosas de fiéis orientados por lideranças fundamentalistas.',
    ' desterritorialização forçada de populações afetadas por conflitos armados.','e'))

msg1 = 'Qual das alternativas apresenta' \
       ' os Presidentes do Brasil em ordem de sucessão?'
enunciado(2,msg1)
print(alternativas('Dilma Rousseff, Lula, Jair Bolsonaro',
    'Fernando Henrique, Itamar Franco, Lula',
    'Itamar Franco, Collor, Lula',
    'Collor, Lula, Dilma Rousseff',
    'Dilma Rousseff, Michel Temer, Jair Bolsonaro',
    'e'))
