# modulo aleatorio
from random import choice

# cores
cores = {'limpa': '\033[m',
       'titulo': '\033[1;4;35m',
         'preto': '\033[30m',
        'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}

# cores aleatorias
cor = ['preto', 'vermelho', 'verde', 'amarelo', 'azul', 'roxo', 'ciano', 'cinza']

# numero de elementos do titulo
t = len('Numeros Primos')+10

# titulo
print('{}{:^{}}{}'.format(cores['titulo'], 'Numeros Primos', t, cores['limpa']))

primo = 0
numero = int(input('Digite um numero: '))
for c in range(2, numero):
    divisao = numero % c
    if divisao == 0:
        primo += 1
if primo == 0 and numero > 1:
    print('O numero {} é um numero {}Primo{}!'.format(numero, cores['verde'], cores['limpa']))
else:
    print('O numero {} Não é um numero {}Primo{}!'.format(numero, cores['vermelho'], cores['limpa']))