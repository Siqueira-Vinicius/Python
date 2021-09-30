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
m = [1, 2, 3]

maquina = choice(m)
print('{}{:^19}{}'.format(cores['titulo'],'JO KEN PO', cores['limpa']))
escolha = int(input('Escolha entre\n[1]{}Pedra{}\n[2]{}Papel{}\n[3]{}Tesoura{}\nR: '
                    .format(cores['cinza'], cores['limpa'], cores['azul'],
                            cores['limpa'], cores['ciano'], cores['limpa'])))
sleep(1)
print('{}JO{}'.format(cores[choice(cor)],cores['limpa']))
sleep(1)
print('{}KEN{}'.format(cores[choice(cor)], cores['limpa']))
sleep(1)
print('{}PO{}'.format(cores[choice(cor)], cores['limpa']))
sleep(1)
if escolha == 1:
    if maquina == 1:
        print('A Máquina também escolheu {}Pedra{}: {}Vocês Empataram!{}'.format(cores['cinza'], cores['limpa'],
                                                                                 cores['amarelo'], cores['limpa']))
    elif maquina == 2:
        print('A Máquina escolheu {}Papel{}: {}Você Perdeu!{}'.format(cores['azul'], cores['limpa'],
                                                                                 cores['vermelho'], cores['limpa']))
    elif maquina == 3:
        print('A Máquina escolheu {}Tesoura{}: {}Você Venceu!{}'.format(cores['ciano'], cores['limpa'],
                                                                                 cores['verde'], cores['limpa']))
elif escolha == 2:
    if maquina == 1:
        print('A Máquina escolheu {}Pedra{}: {}Você Ganhou!{}'.format(cores['cinza'], cores['limpa'],
                                                                                 cores['verde'], cores['limpa']))
    elif maquina == 2:
        print('A Máquina também escolheu {}Papel{}: {}Vocês Empataram!{}'.format(cores['azul'], cores['limpa'],
                                                                                 cores['amarelo'], cores['limpa']))
    elif maquina == 3:
        print('A Máquina escolheu {}Tesoura{}: {}Você Perdeu!{}'.format(cores['ciano'], cores['limpa'],
                                                                                 cores['vermelho'], cores['limpa']))
elif escolha == 3:
    if maquina == 1:
        print('A Máquina escolheu {}Pedra{}: {}Você Perdeu!{}'.format(cores['cinza'], cores['limpa'],
                                                                                 cores['vermelho'], cores['limpa']))
    elif maquina == 2:
        print('A Máquina escolheu {}Papel{}: {}Você Venceu!{}'.format(cores['azul'], cores['limpa'],
                                                                                 cores['verde'], cores['limpa']))
    elif maquina == 3:
        print('A Máquina também escolheu {}Tesoura{}: {}Vocês Empataram!{}'.format(cores['ciano'], cores['limpa'],
                                                                                 cores['amarelo'], cores['limpa']))
else:
    print('{}Escolha Inválida!{}'.format(cores['inverso'], cores['limpa']))

