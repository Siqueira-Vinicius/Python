from random import choice
from time import sleep

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

print('{}{:^23}{}'.format(cores['titulo'], 'Numeros Pares', cores['limpa']))
print('Numeros pares de de 0 a 50:')
sleep(0.5)
for c in range(1,51):
    if c % 2 == 0:
        print('{}{}{}'.format(cores[choice(cor)], c, cores['limpa']))
        sleep(0.5)
print('Fim')
