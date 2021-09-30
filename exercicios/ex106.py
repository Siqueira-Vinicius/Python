def titulo(msg, cor, simb):
    """

    :param msg: o titulo
    :param cor: a cor do fundo
    :param simb: o simbolo q sera usado para circundar o titulo
    :return: retorna o titulo enfeitado
    """
    cr = f'\033[1;4{cor}m'
    lp = f'\033[m'
    print(f'{cr}{simb}'*len(msg))
    print(f'{msg}')
    print(f'{simb}'*len(msg))
    print(f'{lp}', end='')

def topico(msg, cor, simb):
    cr = f'\033[3{cor}m'
    lp = '\033[m'
    mid = f'{cr}{simb}{lp}{msg}'
    return f'{mid}'
from time import sleep
while True:
    titulo(' SISTEMA DE AJUDA PyVINNE ', 2, '~')
    saida = str(input(topico(' Função ou Biblioteca > ', 2, '|'))).strip().lower()
    if saida == 'fim':
        break
    else:
        titulo(f' ACESSANDO O MANUAL DO COMANDO "{saida.upper()}"', 4, '~')
        print(end = '', flush = True)
        sleep(1)
        print('\033[7m')
        help(saida)
        print('\033[m', end ='')
titulo(' FIM DO PROGRAMA ', 1, '~')
