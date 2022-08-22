import random

def letra_a():
    def get_tabuada_10(n):
        print('Tabuada do {}:'.format(n))
        for i in range(1, 11):
            r = n*i
            print(f'{n} x {i} = {r}')
        
    valor = input("Digite um número inteiro: ")
    if type(valor) != int or valor < 0:
        print('Valor inválido!')
    else:
        get_tabuada_10(valor)
        
def letra_b():
    def embaralhar(str):
        return ''.join(random.sample(str, len(str))).lower()
    
    str = input("Digite uma string: ")
    str_embaralhada = embaralhar(str)
    print(str_embaralhada)

print('A - Tabuada do 10 de um número inserido pelo usuário')
letra_a()
print('Fim da letra A')
print('B - Embaralhar uma string inserida pelo usuário')
letra_b()
print('Fim da letra B')
