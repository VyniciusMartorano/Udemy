'''lista = [1,2,3,4,5]
n1, n2 ,*n = lista
print(n1,n2,n)'''
def func(*args):
    args = list(args)
    args[0] = 20
    print(args)

func(1,5,2,6,2)
