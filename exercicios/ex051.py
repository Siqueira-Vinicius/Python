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
t = len('Progressão Aritmética')+10

# titulo
print('{}{:^{}}{}'.format(cores['titulo'], 'Progressão Aritmética', t, cores['limpa']))

primeiro = int(input('Digite o {}primeiro termo{} da {}PA{}: '.format(cores[choice(cor)], cores['limpa'],
                                                                      cores[choice(cor)], cores['limpa'])))
razao = int(input('Digite a {}razão{} da {}PA{}: '.format(cores[choice(cor)], cores['limpa'],
                                                          cores[choice(cor)], cores['limpa'])))
ultimo = primeiro + ((10-1)*razao) + 1
for c in range(primeiro, ultimo, razao):
    print('{}{}{} '.format(cores[choice(cor)], c, cores['limpa']),end='→ ')
print('fim')

