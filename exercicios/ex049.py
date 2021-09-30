cores = {'limpa': '\033[m',
         'titulo': '\033[1;4;35m'}


print('{}{:^17}{}'.format(cores['titulo'], 'TABUADA', cores['limpa']))
n = int(input('Digite um numero: '))

for c in range(1,11):
    print('{:2} x {:2} = {:2}'.format(n, c, n*c))

