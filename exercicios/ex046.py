from time import sleep
from random import choice
cores = {'limpa': '\033[m',
         'titulo': '\033[1;4;35m',
         'preto': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'inverso': '\033[7m'}

cor = ['preto', 'vermelho', 'verde', 'amarelo', 'azul', 'roxo', 'ciano', 'cinza']

print('{}{:^18}{}'.format(cores['titulo'], 'ANO NOVO', cores['limpa']))

print('Contagem Regressiva:')
sleep(1)
for c in range(10, -1, -1):
    print('{}{}{}'.format(cores[choice(cor)], c, cores['limpa']))
    sleep(1)
print('{}FElLIZ ANO NOVO!!!{}'.format(cores[choice(cor)], cores['limpa']))


