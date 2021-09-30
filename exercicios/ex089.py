aluno = []
dados = []
contador = 1
erro = 0
print(f'\033[31m{" MÉDIA DOS ALUNOS ":-^40}\033[m')
while True:
    if contador == 1:
        while True:
            continuar = str(input('Quer cadastrar um aluno?[S][N]: ')).strip()[0]
            if continuar in 'SsNn':
                break
            else:
                print('\033[7m Resposta Inválida.Tente Novamente! \033[m')
        if continuar in 'Nn':
            break
    aluno.append(str(input(f'Digite o nome do {contador}º aluno: ')).strip().capitalize())
    for c in range(1, 3):
        while True:
            aluno.append(float(input(f'Qual a nota de {aluno[-c]} no {c}º semestre?: ')))
            if 0 > aluno[-1] or aluno[-1] > 10:
                print('\033[7m Resposta inválida.Tente novamente! \033[m')
                aluno.pop()
            else:
                break
    dados.append(aluno[:])
    while True:
        continuar = str(input(f'Quer cadastrar mais algum aluno?[S][N]: '))
        if continuar in 'SsNn':
            break
        else:
            print('\033[7m Resposta Inválida.Tente novamente! \033[m')
    if continuar in 'Nn':
        break
    aluno.clear()
    contador += 1
dados.sort()
for n, ordem in enumerate(dados):
    ordem.append(n+1)
    if (ordem[1] + ordem[2])/2 >= 7:
        ordem.append('\033[32mAprovado\033[m')
    else:
        ordem.append('\033[31mReprovado\033[m')
if len(dados) > 0:
    print(f'\033[34m{" BOLETIM ":-^40}\033[m')
    print(f'{"Nº":<5}{"NOME":<15}{"MEDIA":<10}{"STATUS":<10}')
    for a in dados:
        print(f'{a[3]:<5}{a[0]:<15}{(a[1]+a[2])/2:<10.1f}{a[4]:<10}')
    print('\033[34m-\033[m'*40)
contador = 1
while True:
    if contador == 1:
        while True:
            continuar = str(input('Gostaria de ver as notas de algum aluno?[S][N]: ')).strip()[0]
            if continuar in 'SsNn':
                break
            else:
                print('\033[7m Resposta inválida. Tente novamente! \033[m')
    if continuar in 'Ss':
        while True:
            nota = str(input('Digite o nome do aluno: ')).strip().capitalize()
            for d in dados:
                if nota in d:
                    erro = 1
            if erro == 0:
                print('\033[7m Aluno desconhecido. Tente novamente! \033[m')
            else:
                break
        for b in dados:
            if nota in b:
                print(f'\033[35m{" ALUNO ":-^40}\033[m')
                print(f'{"Nº":<5}{"NOME":<15}{"NOTA 1":^10}{"NOTA 2":^10}')
                print(f'{b[3]:<5}{b[0]:<15}{b[1]:^10}{b[2]:^10}')
                print('\033[35m-\033[m'*40)
    else:
        break
    while True:
        continuar = str(input(f'Quer ver a nota de mais algum aluno?[S][N]: '))
        if continuar in 'SsNn':
            break
        else:
            print('\033[7m Resposta Inválida.Tente novamente! \033[m')
    if continuar in 'Nn':
        break
    contador += 1
print(f'\033[31m{" FIM DO PROGRAMA ":-^40}\033[m')