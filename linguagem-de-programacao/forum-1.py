
def getTabuada10(n):
    print('Tabuada do {}:'.format(n))
    for i in range(1, 11):
        r = n*i
        print(f'{n} x {i} = {r}')

valor = input("Digite um número inteiro: ")
if type(valor) != int or valor < 0:
    print('Valor inválido!')
else:
    getTabuada10(valor)
