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
         'cinza': '\033[37m'}

cor = ['preto', 'vermelho', 'verde', 'amarelo', 'azul', 'roxo', 'ciano', 'cinza']
print('{}{:^24}{}'.format(cores['titulo'], 'Soma Dos Pares', cores['limpa']))
s = 0
r = 0
for c in range(1, 7):
    n = int(input('digite o {}{}º{} numero: '.format(cores[choice(cor)], c, cores['limpa'])))
    if 0 != n and n % 2 == 0:
        s += 1
        r += n
print('A soma dos {}{}{} numeros pares digitados é {}{}{}'.format(cores[choice(cor)], s, cores['limpa'],
                                                                   cores[choice(cor)], r, cores['limpa']))


