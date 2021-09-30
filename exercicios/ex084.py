dados = list()
pessoas = list()
pesados = list()
leves = list()
pesos = list()
contador = 1

print(f'\033[1;34m{" MAIOR E MENOR PESO ":-^44}\033[m')

while True:

    if contador == 1:
        while True:
            continuar = str(input('Deseja cadastrar alguem no sistema?[S][N]: '))
            if continuar in 'SsNn':
                break
            else:
                print('Reposta inválida.Tente novamente!')
        if continuar in 'Nn':
            break

    dados.append(str(input(f'Digite o nome da {contador}ª pessoa: ')).strip().capitalize())
    dados.append(float(input(f'Digite o peso de {dados[-1]}(Kg): ')))
    pessoas.append(dados[:])

    while True:
        continuar = str(input('Deseja cadastrar mais alguem?[S][N]: '))
        if continuar in 'SsNn':
            break
        else:
            print('Reposta inválida.Tente novamente!')
    if continuar in 'Nn':
        break
    contador += 1
    dados.clear()

if len(pessoas) == 1:
    print(f'Apenas uma pessoa se cadastrou no sistema: ', end='')
    print(f'{pessoas[0][0]}.')
elif len(pessoas) == 2:
    print(f'{len(pessoas)} Pessoas se cadastraram no sistema: ', end='')
    print(f'{pessoas[0][0]} e {pessoas[1][0]}.')
elif len(pessoas) > 2:
    print(f'{len(pessoas)} Pessoas se cadastraram no sistema: ', end='')
    for c in pessoas[:-2]:
        print(c[0], end=', ')
    print(f'{pessoas[-2][0]} e {pessoas[-1][0]}.')
else:
    print('Nenhuma pessoa se cadastrou no sistema.')

for p in pessoas:
    pesos.append(p[1])
for p1 in pessoas:
    if p1[1] == min(pesos):
        leves.append(p1)
    if p1[1] == max(pesos):
        pesados.append(p1)

if len(pessoas) > 0:
    print(f'O maior peso foi {pesados[0][1]:.1f} Kg de ', end='')
    if len(pesados) == 1:
        print(pesados[0][0])
    elif len(pesados) == 2:
        print(f'{pesados[0][0]} e {pesados[1][0]}.')
    elif len(pesados) > 2:
        for a in pesados[:-2]:
            print(a[0], end=', ')
        print(f'{pesados[-2][0]} e {pesados[-1][0]}.')

    print(f'O menor peso foi {leves[0][1]:.1f} Kg de ', end='')
    if len(leves) == 1:
        print(leves[0][0])
    elif len(leves) == 2:
        print(f'{leves[0][0]} e {leves[1][0]}.')
    elif len(leves) > 2:
        for b in leves[:-2]:
            print(b[0], end=', ')
        print(f'{leves[-2][0]} e {leves[-1][0]}.')

