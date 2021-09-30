jogadores = []
gols = []
jogador = {'Nome': 0}
soma = teste = contador = 0
print(f'\033[32m{" FUTEBOLZINHO DO BINIZIU ":^40}\033[m')
print('\033[32m-\033[m'*40)
while True:
    jogador['Nome'] = str(input(f'\033[32m|\033[mDigite o nome do {contador+1}º jogador: ')).strip().capitalize()
    print('\033[32m-\033[m' * 40)
    n = int(input(f'\033[32m|\033[mQuantas partidas {jogador["Nome"]} jogou?: '))
    print('\033[32m-\033[m' * 40)
    for c in range(1, n+1):
        gols.append(int(input(f'\033[32m|\033[mQuantos gols {jogador["Nome"]} fez no {c}º jogo?: ')))
        print('\033[32m-\033[m' * 40)
        soma += gols[-1]
    jogador['gols'] = gols[:]
    jogador['total de gols'] = soma
    jogadores.append(jogador.copy())
    gols.clear()
    soma = 0
    contador += 1
    while True:
        continuar = str(input('\033[32m|\033[mQuer continuar?[S][N]: ')).strip().upper()[0]
        print('\033[32m-\033[m' * 40)
        if continuar in 'SN':
            break
        else:
            print('\033[7m resposta inválida \033[m')
    if continuar in 'N':
        break
print(f'\033[31m{" JOGADORES ":-^40}\033[m')
print(f'\033[31m|\033[m{"NOME":<20}\033[31m|\033[m{"GOLS":<20}')
print('\033[31m-\033[m'*40)
for c in jogadores:
    for k, v in c.items():
        if k == 'Nome' or k == 'total de gols':
         print(f'\033[31m|\033[m{v:<20}', end='')
    print('')
print('\033[31m-\033[m'*40)
print(f'\033[33m{" DETALHES ":-^40}\033[m')
while True:
    while True:
        quer = str(input('\033[33m|\033[mDigite o nome do jogador que deseja saber mais detalhes\n'
                         '\033[33m|\033[mOBS: digite 0 para encerrar o programa\n\033[33m|\033[mR: ')).strip().capitalize()
        print('\033[33m-\033[m'*40)
        if quer == '0':
            break
        for z in jogadores:
            if quer in z.values():
                teste += 1
        if teste > 0:
            teste = 0
            break
        else:
            print('\033[7m Jogador não cadastrado! \033[m')
    if quer == '0':
        break
    print(f'\033[34m{" JOGADOR ":-^40}\033[m')
    for c in jogadores:
        if quer == c['Nome']:
            for k, v in c.items():
                if k == 'gols':
                    for a, b in enumerate(v):
                        print(f'\033[34m|\033[mNa partida {a+1}, {c["Nome"]} fez {b} gols')
                        print('\033[34m-\033[m' * 40)
                else:
                    print(f'\033[34m|\033[m{k}: {v}')
                    print('\033[34m-\033[m' * 40)
print(f'\033[31m{" FIM DO PROGRAMA ":-^40}\033[m')

