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
s = 0
r = 0
print('{}{:^29}{}'.format(cores['titulo'], 'Matemática Avançada', cores['limpa']))
for c in range(1,501):
    if c % 3 == 0 and c % 2 != 0:
        s += c
        r += 1
print('O resultado da soma dos {}{}{} numeros solicitados foi {}{}{}'.format(cores[choice(cor)],
                                                                             r, cores['limpa'],
                                                                             cores[choice(cor)], s, cores['limpa']))
