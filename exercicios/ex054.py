# modulo aleatorio
from random import choice
from datetime import date
# cores
cores = {'limpa': '\033[m',
       'titulo': '\033[1;4;35m',
         'preto': '\033[1;30m',
        'vermelho': '\01933[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'ciano': '\033[1;36m',
         'cinza': '\033[1;37m'}

# cores aleatorias
cor = ['preto', 'vermelho', 'verde', 'amarelo', 'azul', 'roxo', 'ciano', 'cinza']

# numero de elementos do titulo
t = len('Pesquisa')+35

# titulo
print('{}{:^{}}{}'.format(cores['titulo'], 'Pesquisa', t, cores['limpa']))

anoatual = date.today().year
maioridade = 0
menoridade = 0
for c in range(1,8):
    anonasc = int(input('Em que ano o {}º estrevistado nasceu?: '.format(c)))
    idade = anoatual - anonasc
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print('{} entrevistados são {}Maiores de Idade{} \n{} entrevistados são {}Menores de Idade{}'
      .format(maioridade, cores['azul'], cores['limpa'], menoridade, cores['vermelho'], cores['limpa']))
