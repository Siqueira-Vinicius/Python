aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média desse aluno: '))
if aluno['media'] >= 5:
    aluno['situação'] = '\033[32mAprovado\033[m'
else:
    aluno['situação'] = '\033[31mReprovado\033[m'
for k, v in aluno.items():
    print(f'{k} do aluno é {v}')