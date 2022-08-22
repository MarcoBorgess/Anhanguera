
def getTabuada10(n):
    print('Tabuada do {}:'.format(n))
    for i in range(1, 11):
        r = n*i
        print(f'{n} x {i} = {r}')

valor = int(input("Digite um número: "))
getTabuada10(valor)
