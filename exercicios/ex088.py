from random import randint
from time import sleep
jogos = []
sorteio = []
print(f'\033[1;32m{" Mega Sena ":-^40}\033[m')
n = int(input('Quantos jogos deseja gerar?: '))
for a in range(0, n):
    for b in range(0, 6):
        while True:
            sorteado = randint(1, 60)
            if sorteado not in sorteio:
                sorteio.append(sorteado)
                break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
    sleep(1)
    print(f'Jogo {a+1}: {jogos[-1]}')
sleep(1)
print(f'\033[32m{" Boa Sorte! ":-^40}\033[m')
