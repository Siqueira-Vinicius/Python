print('escolha uma cor')

cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'famarelo':'\033[43m',
         'fazul':'\033[44m',
         'fverde':'\033[42m',
         'fvermelho':'\033[41m',
         'fazuln':'\033[1;44m',
         'famarelon':'\033[1;43m',
         'fvermelhon':'\033[1;41m',
         'fverden':'\033[1;42m',
         'inverter':'\033[7m'}


cor = str(input('escolha entre {}azul{}, {}verde{}, {}vermelho{} e {}amarelo{}: '
    .format(cores['azul'],cores['limpa'],cores['verde'],cores['limpa'],
            cores['vermelho'],cores['limpa'],cores['amarelo'],cores['limpa']))).strip().upper()

if cor == 'AZUL':
    print('{}A cor escolhida foi {}Azul{}'.format(cores['fazul'],cores['fazuln'],cores['limpa']))
elif cor == 'VERMELHO':
    print('{}A cor escolhida foi {}Vermelho{}'.format(cores['fvermelho'],cores['fvermelhon'],cores['limpa']))
elif cor == 'VERDE':
    print('{}A cor escolhida foi {}Verde{}'.format(cores['fverde'],cores['fverden'],cores['limpa']))
elif cor == 'AMARELO':
    print('{}A cor escolhida foi {}Amarelo{}'.format(cores['famarelo'],cores['famarelon'],cores['limpa']))
else:
    print('{}Você não escolheu nenhuma das cores validas{}'.format(cores['inverter'],cores['limpa']))



