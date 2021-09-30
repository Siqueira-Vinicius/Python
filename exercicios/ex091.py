from random import randint
from time import sleep
from operator import itemgetter
jogador = {}
ranking = list()
for c in range(1, 5):
    jogador[c] = randint(1, 6)
    print(f'Jogador {c} tirou {jogador[c]}')
    sleep(1)
print(f'\033[34m{" Ranking ":-^30}\033[m')
ranking = sorted(jogador.items(), key= itemgetter(1), reverse=True)
contador = 1
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: jogador {v[0]} com {v[1]}')
