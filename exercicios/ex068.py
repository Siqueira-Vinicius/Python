cor = {'limpa': '\033[m',
        'titulo': '\033[1;4;35m',
        'preto': '\033[30m',
        'vermelho': '\033[31m',
        'verde': '\033[42m',
        'amarelo': '\033[43m',
        'azul': '\033[34m',
        'roxo': '\033[35m',
        'ciano': '\033[36m',
        'cinza': '\033[37m',
        'inverso': '\033[7m'}

from time import sleep
from random import randint

titulo = 'Par ou Impar'
esp = len(titulo)+35
print('\033[1;4;34m', f'{titulo:^{esp}}', '\033[m')

vitorias = 0
while True:
    parouimpar = int(input(f'Par ou Impar?\n[1]{cor["vermelho"]}Par{cor["limpa"]}\n'
                           f'[2]{cor["ciano"]}Impar{cor["limpa"]}\nR: '))
    if parouimpar == 2 or parouimpar == 1:
        numero = int(input('Digite um numero: '))
        sleep(0.5)
        print(f'{cor["vermelho"]}Par{cor["limpa"]}')
        sleep(1)
        print(f'{cor["roxo"]}ou{cor["limpa"]}')
        sleep(1)
        print(f'{cor["ciano"]}Impar{cor["limpa"]}')
        sleep(1)
        maquina = randint(0, 100)
        resultado = maquina + numero
        if resultado % 2 == 0:
            print(f'A maquina escolheu o numero {maquina}.\n{numero} + {maquina} = {resultado}')
            print(f'{resultado} é um numero Par')
            if parouimpar == 1:
                print(f'{cor["verde"]} Você Venceu! {cor["limpa"]}')
                vitorias += 1
            else:
                print(f'{cor["amarelo"]} Você Perdeu! {cor["limpa"]}')
                break
        else:
            print(f'A maquina escolheu o numero {maquina}.\n{numero} + {maquina} = {resultado}')
            print(f'{resultado} é um numero Impar')
            if parouimpar == 1:
                print(f'{cor["amarelo"]} Você Perdeu! {cor["limpa"]}')
                break
            else:
                print(f'{cor["verde"]} Você Venceu! {cor["limpa"]}')
                vitorias += 1
    else:
        print(f'{cor["inverso"]} Opção Inválida, Tente novamente! {cor["limpa"]}')
print(f'Você venceu {vitorias} Vezes')