'''from time import sleep
x = 0
while x<60:
    x+=1
    print(x)
    sleep(1)
'''

x = 0   #coluna
while x < 10:
    y=0    #linha
    while y < 5:
        print(f'O valor de x é {x} e o valor de y é {y}')
        y += 1
    x += 1
print('FIM')