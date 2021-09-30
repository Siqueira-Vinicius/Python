from random import choice
import home
from home import fund, lp
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
while True:
    home.titulo('JO KEN PO', 4, '-')
    a = choice(lista)
    while True:
        try:
            b = int(input('Escolhe uma opção\n[1] pedra\n[2] papel\n[3] tesoura\nR: '))
        except:
            print('\033[7m Opção Inválida! \033[m')
            continue
        else:
            if b == 1 or b == 2 or b == 3:
                break
            else:
                print('\033[7m Opção Inválida! \033[m')
                continue
    sleep(1)
    print('\033[31mJO\033[m')
    sleep(1)
    print('\033[35mKEN\033[m')
    sleep(1)
    print('\033[34mPO\033[m')
    print(f'Você escolheu {lista[b-1]}')
    print('x')
    print(f'A maquina escolheu {a}')
    if b == 1:
        if a == 'pedra':
            print(f'{fund(3)}Vocês empataram!{lp}')
        elif a == 'papel':
            print(f'{fund(1)}Você Perdeu!{lp}')
        elif a == 'tesoura':
            print(f'{fund(2)}Você Ganhou!{lp}')
    elif b == 2:
        if a == 'pedra':
            print(f'{fund(2)}Você Ganhou!{lp}')
        elif a == 'papel':
            print(f'{fund(3)}Vocês empataram!{lp}')
        elif a == 'tesoura':
            print(f'{fund(1)}Você Perdeu!{lp}')
    elif b == 3:
        if a == 'pedra':
            print(f'{fund(1)}Você Perdeu!{lp}')
        elif a == 'papel':
            print(f'{fund(2)}Você Ganhou!{lp}')
        elif a == 'tesoura':
            print(f'{fund(3)}Vocês empataram!{lp}')
    while True:
        cont = str(input('Quer continuar?[S][N]: ')).strip().upper()[0]
        if cont in 'SN':
            break
        else:
            print('\033[7m Resoista Inválida. Tente novamente! \033[m')
    if cont in 'N':
        break