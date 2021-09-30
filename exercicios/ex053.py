# modulo aleatorio
from random import choice

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
t = len('Palíndromo')+35

# titulo
print('{}{:^{}}{}'.format(cores['titulo'], 'Palíndromo', t, cores['limpa']))

inverso = []
print('Palíndromo: Frase ou palavra que se pode ler,\nindiferentemente, da esquerda para a direita\nou vice-versa.\n')
frase = str(input('Teste se sua frase é um {}Palíndromo{}: '.format(cores['azul'],
                                                                    cores['limpa']))).strip().upper().split()
frase = ''.join(frase)
letras = len(frase)
for d in range(letras-1, -1, -1):
    inverso += frase[d]
inverso = ''.join(inverso)

if inverso == frase:
    print('O inverso de {} é {} \nSua frase é um {}Palíndromo{}!'.format(frase, inverso, cores['verde'], cores['limpa']))
else:
    print('O inverso de {} é {} \nSua frase não é um {}Palíndromo{}!'.format(frase, inverso, cores['vermelho'], cores['limpa']))
