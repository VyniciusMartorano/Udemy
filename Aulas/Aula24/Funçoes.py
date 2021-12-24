def saudação(saud='Olá',nome='Desconhecido'):
    print(f'{saud} {nome}, espero que esteja tudo bem :)')

def soma(n1=0,n2=0,n3=0):
    soma = n1 + n2 + n3
    return float(soma)

def aumento(num=0,perc=0):
    aum = (num/100) * perc + num
    return f'O valor com aumento de {perc}% fica {aum}'

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    return num

print(fizzbuzz(10))

'''def frase(frase):
    return frase
def falar(x):
    print(x)
falar(frase('Hello word'))'''