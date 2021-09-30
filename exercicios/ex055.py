# modulo aleatorio
from random import choice
from datetime import date
# cores
cores = {'limpa': '\033[m',
       'titulo': '\033[1;4;35m',
         'preto': '\033[1;30m',
        'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'ciano': '\033[1;36m',
         'cinza': '\033[1;37m'}

# cores aleatorias
cor = ['preto', 'vermelho', 'verde', 'amarelo', 'azul', 'roxo', 'ciano', 'cinza']

# numero de elementos do titulo
t = len('Pesos')+35

# titulo
print('{}{:^{}}{}'.format(cores['titulo'], 'Pesos', t, cores['limpa']))

maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}º pesso(Kg):'.format(c)))
    if c == 1:
        maior = peso
        menor = peso

    if peso > maior :
        maior = peso

    if peso < menor :
        menor = peso
print('Entre os pesos dessas 5 pessoas, o {}maior{} foi {}Kg e o {}menor{} foi {}Kg'
      .format(cores['verde'], cores['limpa'], maior, cores['azul'], cores['limpa'], menor))
