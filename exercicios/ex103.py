def ficha(nome='desconhecido', gols='0'):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


n = str(input('Nome do jogador: ')).strip().capitalize()
g = str(input('Quantos gols marcou: '))
if n == '':
    if g == '':
        print(ficha())
    else:
        print(ficha(gols = g))
else:
    if g == '':
        print(ficha(nome = n))
    else:
        print(ficha(nome = n, gols = g))
